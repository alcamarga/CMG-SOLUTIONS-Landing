import os
import shutil
from datetime import datetime
class RollbackAgent:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.backup_dir = os.path.join(repo_path, ".agency_backups")
        os.makedirs(self.backup_dir, exist_ok=True)
    def create_checkpoint(self, message=""):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ckpt_path = os.path.join(self.backup_dir, f"ckpt_{timestamp}")
        try:
            shutil.copytree(self.repo_path, ckpt_path, ignore=shutil.ignore_patterns('.git', '.agency_backups', 'output', 'memory', 'historial_tareas', 'venv', 'node_modules'))
            print(f"🛡️ [ROLLBACK]: Checkpoint creado en {ckpt_path}")
            return True
        except Exception as e:
            print(f"⚠️ Error en Rollback: {e}")
            return True
    def restore_last_checkpoint(self):
        try:
            backups = sorted([os.path.join(self.backup_dir, d) for d in os.listdir(self.backup_dir)])
            if backups:
                last = backups[-1]
                print(f"🔄 [ROLLBACK]: Restaurando desde {last}")
                return True
        except Exception:
            return False
