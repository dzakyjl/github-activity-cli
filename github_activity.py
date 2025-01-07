import sys
import urllib.request
import json

def fetch_github_activity(dzakyjl):
  url = f"https://api.github.com/users/dzakyjl/events"
  try:
    with urllib.request.urlopen(url) as response:
      if response.status != 200:
        print(f"Error: Received status code {response.status}")
        return
      data = json.loads(response.read())
      for event in data[:5]:
        event_type = event['type']
        repo_name = event['repo']['name']
        print(f"{event_type} in {repo_name}")
  except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.reason}")
  except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")
  except Exception as e:
    print(f"An error occured: {e}")
    
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: github-activity dzakyjl")
  else:
    username = sys.argv[1]
    fetch_github_activity(username)
    
