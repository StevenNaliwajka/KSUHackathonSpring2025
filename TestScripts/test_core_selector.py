import importlib
import os
import sys


if __name__ == "__main__":
    num_directories = 3
    current_directory = os.path.abspath(__file__)
    up_levels = ['..'] * num_directories
    proj_root = os.path.abspath(os.path.join(current_directory, *up_levels))

    sys.path.append(os.path.abspath(proj_root))

    if len(sys.argv) < 2:
        print("Usage: python test_core_selector.py <file_to_call.py>")
        sys.exit(1)

    file_to_call = sys.argv[1]  # e.g., "test_db_core.py"

    # Strip off .py to get a usable module name
    module_name, _ = os.path.splitext(os.path.basename(file_to_call))

    # Build the absolute path to the file
    script_dir = os.path.dirname(__file__)
    module_path = os.path.join(script_dir, "Core", file_to_call)
    # Adjust "Core" if your directory structure is different

    # Dynamically load the module
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # Now call the function. If your function is also named `test_db_core`,
    # we can try to retrieve it from the loaded module:
    func_to_call = getattr(mod, "test_db_core", None)
    if func_to_call is None:
        print(f"Function 'test_db_core' not found in '{file_to_call}'.")
    else:
        func_to_call()  # Call the function