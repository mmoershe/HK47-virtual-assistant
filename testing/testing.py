import pkg_resources

def get_library_version(library_name):
    try:
        version = pkg_resources.get_distribution(library_name).version
        return version
    except pkg_resources.DistributionNotFound:
        return f"{library_name} is not installed."
    except Exception as e:
        return f"Error retrieving {library_name} version: {e}"

if __name__ == "__main__":
    library_name = "python-telegram-bot"
    version = get_library_version(library_name)
    print(f"{library_name} Version: {version}") 
