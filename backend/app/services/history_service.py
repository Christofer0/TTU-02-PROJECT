from app.repositories.permohonan_repository import PermohonanRepository

class HistoryService:
    """Service for Permohonan operations for Mahasiswa"""

    def __init__(self):
        self.repo_permohonan = PermohonanRepository()

    def get_history_by_status(self, user_id: str, role:str,status: str):
        """Get history of permohonan for a mahasiswa by status"""
        if role == "mahasiswa":
            history = self.repo_permohonan.get_by_mahasiswa(user_id, status)
        elif role == "dosen":
            history = self.repo_permohonan.get_by_dosen(user_id,status)
        elif role == "admin":
            pass
        return history

    def get_counts_by_status(self, user_id: str,role:str):
        """Get counts of permohonan grouped by status for a mahasiswa"""
        # Ambil semua permohonan milik mahasiswa
        if role == "mahasiswa":
            all_permohonan = self.repo_permohonan.get_by_mahasiswa(user_id)
        elif role == "dosen":
            all_permohonan = self.repo_permohonan.get_by_dosen(user_id)
        elif role == "admin":
            pass
        # Hitung jumlah per status
        counts = {
            "pending": 0,
            "disetujui": 0,
            "ditolak": 0,
            "ditandatangani": 0
        }

        for p in all_permohonan:
            status = p.status_permohonan
            if status in counts:
                counts[status] += 1
            else:
                counts[status] = 1  # kalau ada status baru

        return counts

    def get_total_permohonan(self, user_id: str, role:str):
        """Get total permohonan for a mahasiswa"""
        if role == "mahasiswa":
            all_permohonan = self.repo_permohonan.get_by_mahasiswa(user_id)
        elif role == "dosen":
            all_permohonan = self.repo_permohonan.get_by_dosen(user_id)
        return len(all_permohonan)
    
    def get_all_history(self, user_id: str,role:str):
        """Get all permohonan tanpa filter status"""
        if role == "mahasiswa":
            get_all_permohonan = self.repo_permohonan.get_by_mahasiswa(user_id)
        elif role == "dosen":
            get_all_permohonan = self.repo_permohonan.get_by_dosen(user_id)
        elif role == "admin":
            pass
        return get_all_permohonan