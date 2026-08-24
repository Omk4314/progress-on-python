import os
import shutil
from pathlib import Path


class DownloadsOrganizer:
    CATEGORY_MAPPINGS = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Executables": [".exe", ".msi", ".bat", ".sh"],
        "Others": []
    }

    def __init__(self, download_dir: str | Path | None = None):
        """
        Initialize the DownloadsOrganizer with a target downloads directory.
        """
        self.download_dir = Path(download_dir) if download_dir else self.get_download_directory()

    def get_download_directory(self) -> Path:
        """
        Get the path to the user's Downloads directory.
        """
        download_path = Path.home() / "Downloads"
        if not download_path.exists():
            print("Downloads directory not found.")
        return download_path

    def create_category_directories(self) -> None:
        """
        Create target category subfolders inside the download directory if they do not exist.
        """
        for category in self.CATEGORY_MAPPINGS.keys():
            category_dir = self.download_dir / category
            category_dir.mkdir(parents=True, exist_ok=True)

    def get_category_for_file(self, file_path: Path) -> str:
        """
        Determine the category for a given file based on its extension.
        """
        ext = file_path.suffix.lower()
        for category, extensions in self.CATEGORY_MAPPINGS.items():
            if ext in extensions:
                return category
        return "Others"

    def scan_downloads_folder(self) -> list[Path]:
        """
        Scan the downloads directory and return a list of files to organize.
        """
        file_paths = []
        if not self.download_dir.exists():
            return file_paths

        for entry in self.download_dir.iterdir():
            if entry.is_file() and not entry.name.startswith('.'):
                file_paths.append(entry)
        return file_paths

    def move_file_to_category(self, file_path: Path, target_dir: Path) -> None:
        """
        Safely move a file to its target category directory, handling potential name collisions.
        """
        if not target_dir.exists():
            print(f"Target directory '{target_dir}' not found.")
            return

        target_file_path = target_dir / file_path.name
        try:
            shutil.move(str(file_path), str(target_file_path))
        except FileExistsError:
            print(f"Error: {target_file_path} already exists.")
        except OSError as e:
            print(f"Error moving {file_path.name}: {e}")

    def organize_downloads(self) -> None:
        """
        Orchestrate the overall process of scanning, categorizing, and moving files.
        """
        self.create_category_directories()
        file_paths = self.scan_downloads_folder()
        for file_path in file_paths:
            category = self.get_category_for_file(file_path)
            target_dir = self.download_dir / category
            self.move_file_to_category(file_path, target_dir)


def main() -> None:
    """
    Main entry point for running the Downloads Manager.
    """
    organizer = DownloadsOrganizer()
    organizer.organize_downloads()
    print("Downloads Manager completed organization.")


if __name__ == "__main__":
    main()
