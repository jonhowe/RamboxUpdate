import requests
import subprocess
import os
import signal

def get_latest_release(repo):
    """
    Fetch the latest release from the GitHub repository.
    
    :param repo: String representing the GitHub repository in the format 'owner/repo'.
    :return: Dictionary with the latest release information or None if an error occurs.
    """
    api_url = f"https://api.github.com/repos/{repo}/releases/latest"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch the latest release")
        return None

def download_file(url, filename):
    """
    Download file from the provided URL.
    
    :param url: URL to download the file from.
    :param filename: Name of the file to save the download as.
    """
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Downloaded {filename}")
    else:
        print("Failed to download the file")

def find_deb_asset(assets):
    """
    Find a .deb asset in the list of assets.
    
    :param assets: List of asset dictionaries as returned by the GitHub API.
    :return: Dictionary of the .deb asset or None if not found.
    """
    for asset in assets:
        if asset['name'].endswith('.deb'):
            return asset
    return None

def kill_process(process_path):
    """
    Kills processes running at the specified path.
    
    :param process_path: Path of the process to be killed.
    """
    try:
        # Find PIDs of the process
        pids = subprocess.check_output(["pidof", "-x", process_path]).decode().strip().split()
        if pids:
            for pid in pids:
                os.kill(int(pid), signal.SIGTERM)
                print(f"Process at {process_path} with PID {pid} has been terminated.")
        else:
            print("No process found running at the specified path.")
    except subprocess.CalledProcessError:
        print("No process found running at the specified path.")
    except ValueError as e:
        print(f"Error processing PID: {e}")

def install_deb_package(filename):
    """
    Install a .deb package using dpkg.
    
    :param filename: The filename of the .deb package to install.
    """
    try:
        subprocess.check_call(["sudo", "dpkg", "-i", filename])
        print(f"Installed the package: {filename}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install the package: {e}")

# Main execution
if __name__ == "__main__":
    repository = "ramboxapp/download"
    process_path = "/opt/Rambox/rambox"

    # Kill the process if it's running
    kill_process(process_path)

    # Get the latest release
    latest_release = get_latest_release(repository)
    if latest_release:
        # Find the .deb asset in the release
        deb_asset = find_deb_asset(latest_release['assets'])
        if deb_asset:
            download_url = deb_asset['browser_download_url']
            asset_name = deb_asset['name']

            # Download the .deb asset
            download_file(download_url, asset_name)

            # Install the .deb package
            install_deb_package(asset_name)
        else:
            print("No .deb package found in the latest release.")
