<template>
  <div class="space-y-4">
    <!-- File Upload Button -->
    <div v-if="!imageUploaded" class="space-y-2">
      <input
        ref="fileInput"
        type="file"
        accept="image/png,image/jpeg,image/jpg,image/gif"
        @change="onFileSelect"
        class="hidden"
      />

      <button
        type="button"
        @click="triggerFileInput"
        class="w-full border-2 border-dashed border-gray-300 rounded-lg p-6 text-center hover:border-green-500 transition-colors cursor-pointer"
      >
        <svg
          class="mx-auto h-12 w-12 text-gray-400"
          stroke="currentColor"
          fill="none"
          viewBox="0 0 48 48"
        >
          <path
            d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
        <p class="mt-2 text-sm text-gray-600">
          <span class="font-medium text-green-600">Klik untuk upload</span>
          tanda tangan
        </p>
        <p class="text-xs text-gray-500 mt-1">PNG, JPG, GIF (min. 200x100px)</p>
      </button>
    </div>

    <!-- Editor Canvas -->
    <div v-else class="space-y-4">
      <!-- Info Alert -->
      <div
        class="bg-blue-50 border border-blue-200 rounded-lg p-3 text-sm text-blue-800"
      >
        <p>
          <strong>Instruksi:</strong> Drag tanda tangan untuk mengatur posisi.
          Gunakan slider untuk zoom.
        </p>
      </div>

      <!-- Canvas Container -->
      <div
        class="border-2 border-gray-300 rounded-lg overflow-hidden bg-gray-50 relative"
      >
        <canvas
          ref="canvas"
          :width="724"
          :height="344"
          class="cursor-move w-full"
          @mousedown="startDrag"
          @mousemove="onDrag"
          @mouseup="stopDrag"
          @mouseleave="stopDrag"
          @touchstart="startDrag"
          @touchmove="onDrag"
          @touchend="stopDrag"
        ></canvas>
      </div>

      <!-- Controls -->
      <div class="space-y-3">
        <!-- Zoom Control -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">
            Ukuran: {{ Math.round(scale * 100) }}%
          </label>
          <input
            type="range"
            v-model.number="scale"
            min="0.2"
            max="2"
            step="0.1"
            @input="redraw"
            class="w-full"
          />
        </div>

        <!-- Position Info -->
        <div class="grid grid-cols-2 gap-2 text-xs text-gray-600">
          <div>X: {{ Math.round(signatureX) }}px</div>
          <div>Y: {{ Math.round(signatureY) }}px</div>
        </div>

        <!-- Action Buttons -->
        <div class="flex gap-2">
          <button
            type="button"
            @click="resetPosition"
            class="flex-1 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 text-sm"
          >
            Reset Posisi
          </button>
          <button
            type="button"
            @click="removeImage"
            class="flex-1 px-4 py-2 border border-red-300 text-red-600 rounded-lg hover:bg-red-50 text-sm"
          >
            Ganti Gambar
          </button>
        </div>
      </div>

      <!-- Error Message -->
      <div
        v-if="error"
        class="bg-red-50 border border-red-200 rounded-lg p-3 text-sm text-red-800"
      >
        {{ error }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";

// =========================
// Props & Emits
// =========================
interface Props {
  modelValue: File | null;
}

interface Emits {
  (e: "update:modelValue", value: File | null): void;
  (e: "update:finalImage", value: Blob | null): void;
}

const props = defineProps<Props>();
const emit = defineEmits<Emits>();

// =========================
// State
// =========================
const fileInput = ref<HTMLInputElement | null>(null);
const canvas = ref<HTMLCanvasElement | null>(null);
const imageUploaded = ref(false);
const error = ref("");

const signatureImage = ref<HTMLImageElement | null>(null);
const signatureX = ref(0);
const signatureY = ref(0);
const scale = ref(1);

const isDragging = ref(false);
const dragStartX = ref(0);
const dragStartY = ref(0);

// =========================
// Constants
// =========================
const TARGET_WIDTH = 724;
const TARGET_HEIGHT = 344;
const MIN_IMAGE_WIDTH = 200;
const MIN_IMAGE_HEIGHT = 100;

// =========================
// File Upload
// =========================
const triggerFileInput = () => {
  fileInput.value?.click();
};

const onFileSelect = (event: Event) => {
  const input = event.target as HTMLInputElement;
  if (!input.files?.length) return;

  const file = input.files[0];
  validateAndLoadImage(file);
};

const validateAndLoadImage = (file: File) => {
  error.value = "";

  // Validate file type
  const allowedTypes = ["image/png", "image/jpeg", "image/jpg", "image/gif"];
  if (!allowedTypes.includes(file.type)) {
    error.value = "File harus berformat PNG, JPG, atau GIF";
    return;
  }

  // Validate file size (max 5MB)
  const maxSize = 5 * 1024 * 1024;
  if (file.size > maxSize) {
    error.value = "Ukuran file maksimal 5MB";
    return;
  }

  // Load and validate image dimensions
  const img = new Image();
  const reader = new FileReader();

  reader.onload = (e) => {
    img.src = e.target?.result as string;
  };

  img.onload = () => {
    // Validate minimum dimensions
    if (img.width < MIN_IMAGE_WIDTH || img.height < MIN_IMAGE_HEIGHT) {
      error.value = `Ukuran gambar terlalu kecil. Minimum ${MIN_IMAGE_WIDTH}x${MIN_IMAGE_HEIGHT}px`;
      return;
    }

    // Image is valid, proceed
    signatureImage.value = img;
    imageUploaded.value = true;

    // Calculate initial position (center)
    const scaledWidth = img.width * scale.value;
    const scaledHeight = img.height * scale.value;
    signatureX.value = (TARGET_WIDTH - scaledWidth) / 2;
    signatureY.value = (TARGET_HEIGHT - scaledHeight) / 2;

    // Auto-scale if image is too large
    if (img.width > TARGET_WIDTH || img.height > TARGET_HEIGHT) {
      const scaleX = TARGET_WIDTH / img.width;
      const scaleY = TARGET_HEIGHT / img.height;
      scale.value = Math.min(scaleX, scaleY) * 0.8; // 80% of max to leave some margin
    }

    emit("update:modelValue", file);

    // Draw on canvas
    setTimeout(() => redraw(), 100);
  };

  img.onerror = () => {
    error.value = "Gagal memuat gambar. Pastikan file valid.";
  };

  reader.readAsDataURL(file);
};

// =========================
// Canvas Drawing
// =========================
const redraw = () => {
  if (!canvas.value || !signatureImage.value) return;

  const ctx = canvas.value.getContext("2d");
  if (!ctx) return;

  // Clear canvas
  ctx.clearRect(0, 0, TARGET_WIDTH, TARGET_HEIGHT);

  // Draw background (white)
  ctx.fillStyle = "#ffffff";
  ctx.fillRect(0, 0, TARGET_WIDTH, TARGET_HEIGHT);

  // Draw grid (optional, for positioning help)
  ctx.strokeStyle = "#e5e7eb";
  ctx.lineWidth = 1;

  // Vertical lines
  for (let x = 0; x <= TARGET_WIDTH; x += TARGET_WIDTH / 4) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, TARGET_HEIGHT);
    ctx.stroke();
  }

  // Horizontal lines
  for (let y = 0; y <= TARGET_HEIGHT; y += TARGET_HEIGHT / 4) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(TARGET_WIDTH, y);
    ctx.stroke();
  }

  // Draw signature image
  const scaledWidth = signatureImage.value.width * scale.value;
  const scaledHeight = signatureImage.value.height * scale.value;

  ctx.drawImage(
    signatureImage.value,
    signatureX.value,
    signatureY.value,
    scaledWidth,
    scaledHeight
  );

  // Generate final image and emit
  generateFinalImage();
};

// =========================
// Drag & Drop for Positioning
// =========================
const startDrag = (e: MouseEvent | TouchEvent) => {
  isDragging.value = true;

  const rect = canvas.value?.getBoundingClientRect();
  if (!rect) return;

  if (e instanceof MouseEvent) {
    dragStartX.value = e.clientX - rect.left - signatureX.value;
    dragStartY.value = e.clientY - rect.top - signatureY.value;
  } else {
    const touch = e.touches[0];
    dragStartX.value = touch.clientX - rect.left - signatureX.value;
    dragStartY.value = touch.clientY - rect.top - signatureY.value;
  }
};

const onDrag = (e: MouseEvent | TouchEvent) => {
  if (!isDragging.value || !signatureImage.value) return;

  const rect = canvas.value?.getBoundingClientRect();
  if (!rect) return;

  let clientX, clientY;

  if (e instanceof MouseEvent) {
    clientX = e.clientX;
    clientY = e.clientY;
  } else {
    const touch = e.touches[0];
    clientX = touch.clientX;
    clientY = touch.clientY;
  }

  const newX = clientX - rect.left - dragStartX.value;
  const newY = clientY - rect.top - dragStartY.value;

  // Constrain within canvas bounds
  const scaledWidth = signatureImage.value.width * scale.value;
  const scaledHeight = signatureImage.value.height * scale.value;

  signatureX.value = Math.max(
    -scaledWidth * 0.2,
    Math.min(TARGET_WIDTH - scaledWidth * 0.8, newX)
  );
  signatureY.value = Math.max(
    -scaledHeight * 0.2,
    Math.min(TARGET_HEIGHT - scaledHeight * 0.8, newY)
  );

  redraw();
};

const stopDrag = () => {
  isDragging.value = false;
};

// =========================
// Controls
// =========================
const resetPosition = () => {
  if (!signatureImage.value) return;

  const scaledWidth = signatureImage.value.width * scale.value;
  const scaledHeight = signatureImage.value.height * scale.value;

  signatureX.value = (TARGET_WIDTH - scaledWidth) / 2;
  signatureY.value = (TARGET_HEIGHT - scaledHeight) / 2;
  scale.value = 1;

  redraw();
};

const removeImage = () => {
  imageUploaded.value = false;
  signatureImage.value = null;
  error.value = "";
  emit("update:modelValue", null);
  emit("update:finalImage", null);

  if (fileInput.value) {
    fileInput.value.value = "";
  }
};

// =========================
// Generate Final Image
// =========================
const generateFinalImage = () => {
  if (!canvas.value) return;

  canvas.value.toBlob(
    (blob) => {
      if (blob) {
        emit("update:finalImage", blob);
      }
    },
    "image/png",
    0.95
  );
};

// =========================
// Watch for scale changes
// =========================
watch(scale, () => {
  redraw();
});
</script>

<style scoped>
canvas {
  max-width: 100%;
  height: auto;
  display: block;
}
</style>
