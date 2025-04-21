from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE : str
    unzip_data_dir: Path
    all_schema : dict

@dataclass
class DataTransformationConfig:
    root_dir : Path
    data_dir : Path
    
@dataclass
class modelTrainerConfig:
    root_dir : Path
    train_data_dir : Path
    test_data_dir : Path
    model_name : str
    aplha : float
    l1_ratio : float
    target_column : str