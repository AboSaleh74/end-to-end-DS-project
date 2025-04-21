import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from typing import Any
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(yaml_file_path : Path) -> ConfigBox:
    """
    read a yaml file
    
    Args:
        file_path (str): path to the yaml file
        
    raises:
        ValueError: if yaml file is empty
        e: empty yaml file
        
    Returns:
        ConfigBox: ConfigBox object containing the yaml file data
        
    """
    try:
        with open(yaml_file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {yaml_file_path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"yaml file: {yaml_file_path} is empty") from e
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
                
@ensure_annotations
def save_json(path: Path, data: dict, verbose = True):
    """
    Save a dictionary as a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        data (dict): Dictionary to be saved.
        ignore_log (bool): If True, do not log the saving of the JSON file.
        
    Returns:
        None
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
        if verbose:
            logger.info(f"saved json file at: {path}")
        
        
@ensure_annotations
def load_json(path: Path, verbose = True) -> dict:
    """
    Load a JSON file and return its content as a dictionary.
    
    Args:
        path (Path): Path to the JSON file.
        ignore_log (bool): If True, do not log the loading of the JSON file.
        
    Returns:
        dict: Content of the JSON file as a dictionary.
    """
    with open(path) as json_file:
        data = json.load(json_file)
        if verbose:
            logger.info(f"loaded json file at: {path}")
        return ConfigBox(data)

@ensure_annotations
def save_bin(data:Any , path:Path ):
    """
    Save data to a binary file using joblib.
    
    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file.
        
    Returns:
        None
    """
    joblib.dump(value = data, filename = path)
    logger.info(f"saved binary file at: {path}")
    