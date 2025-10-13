<template>
  <div class="space-y-4">
    <!-- Mode Selection -->
    <div class="flex gap-2 p-1 bg-gray-100 rounded-lg">
      <button
        type="button"
        @click="mode = 'draw'"
        :class="[
          'flex-1 py-2 px-4 rounded-md text-sm font-medium transition-colors',
          mode === 'draw'
            ? 'bg-white text-green-600 shadow-sm'
            : 'text-gray-600 hover:text-gray-900',
        ]"
      >
        <div class="flex items-center justify-center gap-2">
          <svg
            class="w-4 h-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
            />
          </svg>
          Gambar Sendiri
        </div>
      </button>
      <button
        type="button"
        @click="mode = 'upload'"
        :class="[
          'flex-1 py-2 px-4 rounded-md text-sm font-medium transition-colors',
          mode === 'upload'
            ? 'bg-white text-green-600 shadow-sm'
            : 'text-gray-600 hover:text-gray-900',
        ]"
      >
        <div class="flex items-center justify-center gap-2">
          <svg
            class="w-4 h-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
            />
          </svg>
          Upload Gambar
        </div>
      </button>
    </div>

    <!-- Draw Mode -->
    <div v-if="mode === 'draw'" class="space-y-4">
      <!-- Info Alert -->
      <div
        class="bg-blue-50 border border-blue-200 rounded-lg p-3 text-sm text-blue-800"
      >
        <p>
          <strong>Tips:</strong> Gambar tanda tangan Anda dengan mouse/touchpad.
          Gunakan tombol untuk mengatur.
        </p>
      </div>

      <!-- Drawing Canvas -->
      <div
        class="border-2 border-gray-300 rounded-lg overflow-hidden bg-white relative"
      >
        <canvas
          ref="drawCanvas"
          :width="724"
          :height="344"
          class="w-full cursor-crosshair"
          @mousedown="startDrawing"
          @mousemove="draw"
          @mouseup="stopDrawing"
          @mouseleave="stopDrawing"
          @touchstart="startDrawing"
          @touchmove="draw"
          @touchend="stopDrawing"
        ></canvas>
      </div>

      <!-- Drawing Controls -->
      <div class="space-y-3">
        <!-- Pen Settings -->
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-medium text-gray-700 mb-1">
              Ketebalan: {{ penSize }}px
            </label>
            <input
              type="range"
              v-model.number="penSize"
              min="1"
              max="10"
              class="w-full"
            />
          </div>
          <div>
            <label class="block text-xs font-medium text-gray-700 mb-1">
              Warna
            </label>
            <div class="flex gap-2">
              <button
                type="button"
                @click="penColor = '#000000'"
                :class="[
                  'w-8 h-8 rounded border-2',
                  penColor === '#000000'
                    ? 'border-green-500 scale-110'
                    : 'border-gray-300',
                ]"
                style="background: #000000"
              ></button>
              <button
                type="button"
                @click="penColor = '#0000FF'"
                :class="[
                  'w-8 h-8 rounded border-2',
                  penColor === '#0000FF'
                    ? 'border-green-500 scale-110'
                    : 'border-gray-300',
                ]"
                style="background: #0000ff"
              ></button>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex gap-2">
          <button
            type="button"
            @click="clearDrawing"
            class="flex-1 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 text-sm"
          >
            Hapus Semua
          </button>
          <button
            type="button"
            @click="undoDrawing"
            class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 text-sm"
            :disabled="drawingHistory.length === 0"
          >
            Undo
          </button>
        </div>
      </div>
    </div>

    <!-- Upload Mode -->
    <div v-else-if="mode === 'upload'" class="space-y-4">
      <!-- File Upload or Editor -->
      <div v-if="!uploadedImage">
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
          <p class="text-xs text-gray-500 mt-1">
            PNG, JPG, GIF (min. 200x100px)
          </p>
        </button>
      </div>

      <!-- Upload Editor -->
      <div v-else class="space-y-4">
        <div
          class="bg-blue-50 border border-blue-200 rounded-lg p-3 text-sm text-blue-800"
        >
          <p>
            <strong>Instruksi:</strong> Drag tanda tangan untuk mengatur posisi.
            Gunakan slider untuk zoom.
          </p>
        </div>

        <!-- Upload Canvas -->
        <div
          class="border-2 border-gray-300 rounded-lg overflow-hidden bg-gray-50 relative"
        >
          <canvas
            ref="uploadCanvas"
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

        <!-- Upload Controls -->
        <div class="space-y-3">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Ukuran: {{ Math.round(uploadScale * 100) }}%
            </label>
            <input
              type="range"
              v-model.number="uploadScale"
              min="0.2"
              max="2"
              step="0.1"
              @input="redrawUpload"
              class="w-full"
            />
          </div>

          <div class="grid grid-cols-2 gap-2 text-xs text-gray-600">
            <div>X: {{ Math.round(uploadX) }}px</div>
            <div>Y: {{ Math.round(uploadY) }}px</div>
          </div>

          <div class="flex gap-2">
            <button
              type="button"
              @click="resetUploadPosition"
              class="flex-1 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 text-sm"
            >
              Reset Posisi
            </button>
            <button
              type="button"
              @click="removeUploadedImage"
              class="flex-1 px-4 py-2 border border-red-300 text-red-600 rounded-lg hover:bg-red-50 text-sm"
            >
              Ganti Gambar
            </button>
          </div>
        </div>
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
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from "vue";

// =========================
// Props & Emits
// =========================
interface Emits {
  (e: "update:finalImage", value: Blob | null): void;
}

const emit = defineEmits<Emits>();

// =========================
// State
// =========================
const mode = ref<"draw" | "upload">("draw");

// Drawing mode
const drawCanvas = ref<HTMLCanvasElement | null>(null);
const isDrawing = ref(false);
const penSize = ref(3);
const penColor = ref("#000000");
const drawingHistory = ref<ImageData[]>([]);
const lastX = ref(0);
const lastY = ref(0);

// Upload mode
const fileInput = ref<HTMLInputElement | null>(null);
const uploadCanvas = ref<HTMLCanvasElement | null>(null);
const uploadedImage = ref<HTMLImageElement | null>(null);
const uploadX = ref(0);
const uploadY = ref(0);
const uploadScale = ref(1);
const isDragging = ref(false);
const dragStartX = ref(0);
const dragStartY = ref(0);

const error = ref("");

// Constants
const TARGET_WIDTH = 724;
const TARGET_HEIGHT = 344;
const MIN_IMAGE_WIDTH = 200;
const MIN_IMAGE_HEIGHT = 100;

// =========================
// Drawing Mode Functions
// =========================
const startDrawing = (e: MouseEvent | TouchEvent) => {
  if (mode.value !== "draw" || !drawCanvas.value) return;

  isDrawing.value = true;
  const rect = drawCanvas.value.getBoundingClientRect();

  if (e instanceof MouseEvent) {
    lastX.value = (e.clientX - rect.left) * (TARGET_WIDTH / rect.width);
    lastY.value = (e.clientY - rect.top) * (TARGET_HEIGHT / rect.height);
  } else {
    const touch = e.touches[0];
    lastX.value = (touch.clientX - rect.left) * (TARGET_WIDTH / rect.width);
    lastY.value = (touch.clientY - rect.top) * (TARGET_HEIGHT / rect.height);
    e.preventDefault();
  }

  // Save state for undo
  const ctx = drawCanvas.value.getContext("2d");
  if (ctx) {
    drawingHistory.value.push(
      ctx.getImageData(0, 0, TARGET_WIDTH, TARGET_HEIGHT)
    );
    if (drawingHistory.value.length > 20) {
      drawingHistory.value.shift();
    }
  }
};

const draw = (e: MouseEvent | TouchEvent) => {
  if (!isDrawing.value || mode.value !== "draw" || !drawCanvas.value) return;

  const ctx = drawCanvas.value.getContext("2d");
  if (!ctx) return;

  const rect = drawCanvas.value.getBoundingClientRect();
  let currentX, currentY;

  if (e instanceof MouseEvent) {
    currentX = (e.clientX - rect.left) * (TARGET_WIDTH / rect.width);
    currentY = (e.clientY - rect.top) * (TARGET_HEIGHT / rect.height);
  } else {
    const touch = e.touches[0];
    currentX = (touch.clientX - rect.left) * (TARGET_WIDTH / rect.width);
    currentY = (touch.clientY - rect.top) * (TARGET_HEIGHT / rect.height);
    e.preventDefault();
  }

  ctx.strokeStyle = penColor.value;
  ctx.lineWidth = penSize.value;
  ctx.lineCap = "round";
  ctx.lineJoin = "round";

  ctx.beginPath();
  ctx.moveTo(lastX.value, lastY.value);
  ctx.lineTo(currentX, currentY);
  ctx.stroke();

  lastX.value = currentX;
  lastY.value = currentY;

  generateFinalImage();
};

const stopDrawing = () => {
  isDrawing.value = false;
};

const clearDrawing = () => {
  if (!drawCanvas.value) return;
  const ctx = drawCanvas.value.getContext("2d");
  if (!ctx) return;

  ctx.fillStyle = "#ffffff";
  ctx.fillRect(0, 0, TARGET_WIDTH, TARGET_HEIGHT);
  drawingHistory.value = [];
  generateFinalImage();
};

const undoDrawing = () => {
  if (drawingHistory.value.length === 0 || !drawCanvas.value) return;

  const ctx = drawCanvas.value.getContext("2d");
  if (!ctx) return;

  const lastState = drawingHistory.value.pop();
  if (lastState) {
    ctx.putImageData(lastState, 0, 0);
  } else {
    clearDrawing();
  }

  generateFinalImage();
};

// Initialize drawing canvas
const initDrawCanvas = () => {
  if (!drawCanvas.value) return;
  const ctx = drawCanvas.value.getContext("2d");
  if (!ctx) return;

  ctx.fillStyle = "#ffffff";
  ctx.fillRect(0, 0, TARGET_WIDTH, TARGET_HEIGHT);
};

// =========================
// Upload Mode Functions
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

  const allowedTypes = ["image/png", "image/jpeg", "image/jpg", "image/gif"];
  if (!allowedTypes.includes(file.type)) {
    error.value = "File harus berformat PNG, JPG, atau GIF";
    return;
  }

  const maxSize = 5 * 1024 * 1024;
  if (file.size > maxSize) {
    error.value = "Ukuran file maksimal 5MB";
    return;
  }

  const img = new Image();
  const reader = new FileReader();

  reader.onload = (e) => {
    img.src = e.target?.result as string;
  };

  img.onload = () => {
    if (img.width < MIN_IMAGE_WIDTH || img.height < MIN_IMAGE_HEIGHT) {
      error.value = `Ukuran gambar terlalu kecil. Minimum ${MIN_IMAGE_WIDTH}x${MIN_IMAGE_HEIGHT}px`;
      return;
    }

    uploadedImage.value = img;

    const scaledWidth = img.width * uploadScale.value;
    const scaledHeight = img.height * uploadScale.value;
    uploadX.value = (TARGET_WIDTH - scaledWidth) / 2;
    uploadY.value = (TARGET_HEIGHT - scaledHeight) / 2;

    if (img.width > TARGET_WIDTH || img.height > TARGET_HEIGHT) {
      const scaleX = TARGET_WIDTH / img.width;
      const scaleY = TARGET_HEIGHT / img.height;
      uploadScale.value = Math.min(scaleX, scaleY) * 0.8;
    }

    setTimeout(() => redrawUpload(), 100);
  };

  img.onerror = () => {
    error.value = "Gagal memuat gambar";
  };

  reader.readAsDataURL(file);
};

const redrawUpload = () => {
  if (!uploadCanvas.value || !uploadedImage.value) return;

  const ctx = uploadCanvas.value.getContext("2d");
  if (!ctx) return;

  ctx.fillStyle = "#ffffff";
  ctx.fillRect(0, 0, TARGET_WIDTH, TARGET_HEIGHT);

  // Grid
  ctx.strokeStyle = "#e5e7eb";
  ctx.lineWidth = 1;

  for (let x = 0; x <= TARGET_WIDTH; x += TARGET_WIDTH / 4) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, TARGET_HEIGHT);
    ctx.stroke();
  }

  for (let y = 0; y <= TARGET_HEIGHT; y += TARGET_HEIGHT / 4) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(TARGET_WIDTH, y);
    ctx.stroke();
  }

  const scaledWidth = uploadedImage.value.width * uploadScale.value;
  const scaledHeight = uploadedImage.value.height * uploadScale.value;

  ctx.drawImage(
    uploadedImage.value,
    uploadX.value,
    uploadY.value,
    scaledWidth,
    scaledHeight
  );

  generateFinalImage();
};

const startDrag = (e: MouseEvent | TouchEvent) => {
  if (mode.value !== "upload" || !uploadCanvas.value) return;

  isDragging.value = true;

  const rect = uploadCanvas.value.getBoundingClientRect();

  if (e instanceof MouseEvent) {
    dragStartX.value = e.clientX - rect.left - uploadX.value;
    dragStartY.value = e.clientY - rect.top - uploadY.value;
  } else {
    const touch = e.touches[0];
    dragStartX.value = touch.clientX - rect.left - uploadX.value;
    dragStartY.value = touch.clientY - rect.top - uploadY.value;
    e.preventDefault();
  }
};

const onDrag = (e: MouseEvent | TouchEvent) => {
  if (!isDragging.value || !uploadedImage.value || !uploadCanvas.value) return;

  const rect = uploadCanvas.value.getBoundingClientRect();
  let clientX, clientY;

  if (e instanceof MouseEvent) {
    clientX = e.clientX;
    clientY = e.clientY;
  } else {
    const touch = e.touches[0];
    clientX = touch.clientX;
    clientY = touch.clientY;
    e.preventDefault();
  }

  const newX = clientX - rect.left - dragStartX.value;
  const newY = clientY - rect.top - dragStartY.value;

  const scaledWidth = uploadedImage.value.width * uploadScale.value;
  const scaledHeight = uploadedImage.value.height * uploadScale.value;

  uploadX.value = Math.max(
    -scaledWidth * 0.2,
    Math.min(TARGET_WIDTH - scaledWidth * 0.8, newX)
  );
  uploadY.value = Math.max(
    -scaledHeight * 0.2,
    Math.min(TARGET_HEIGHT - scaledHeight * 0.8, newY)
  );

  redrawUpload();
};

const stopDrag = () => {
  isDragging.value = false;
};

const resetUploadPosition = () => {
  if (!uploadedImage.value) return;

  const scaledWidth = uploadedImage.value.width * uploadScale.value;
  const scaledHeight = uploadedImage.value.height * uploadScale.value;

  uploadX.value = (TARGET_WIDTH - scaledWidth) / 2;
  uploadY.value = (TARGET_HEIGHT - scaledHeight) / 2;
  uploadScale.value = 1;

  redrawUpload();
};

const removeUploadedImage = () => {
  uploadedImage.value = null;
  if (fileInput.value) {
    fileInput.value.value = "";
  }
  emit("update:finalImage", null);
};

// =========================
// Generate Final Image
// =========================
const generateFinalImage = () => {
  const canvas = mode.value === "draw" ? drawCanvas.value : uploadCanvas.value;
  if (!canvas) return;

  canvas.toBlob(
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
// Watch Mode Changes
// =========================
watch(mode, (newMode) => {
  error.value = "";
  if (newMode === "draw") {
    setTimeout(() => initDrawCanvas(), 50);
  }
  emit("update:finalImage", null);
});

watch(uploadScale, () => {
  if (mode.value === "upload") {
    redrawUpload();
  }
});

// =========================
// Initialize
// =========================
onMounted(() => {
  initDrawCanvas();
});
</script>

<style scoped>
canvas {
  max-width: 100%;
  height: auto;
  display: block;
}
</style>
