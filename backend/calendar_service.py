# # import datetime
# # import os.path
# # from google.oauth2.credentials import Credentials
# # from google_auth_oauthlib.flow import InstalledAppFlow
# # from googleapiclient.discovery import build

# # SCOPES = ["https://www.googleapis.com/auth/calendar"]
# # REDIRECT_URI = "http://localhost:5500/oauth2callback"  # Must match Google Cloud Console

# # def add_to_calendar(user_email, roadmap_text, deadline_str):
# #     # Format deadline
# #     deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d")
# #     start_time = deadline - datetime.timedelta(days=7)
# #     end_time = deadline

# #     creds = None
# #     token_path = "backend/token.json"

# #     if os.path.exists(token_path):
# #         creds = Credentials.from_authorized_user_file(token_path, SCOPES)
# #     else:
# #         # ✅ Create flow and pass redirect_uri here
# #         flow = InstalledAppFlow.from_client_secrets_file(
# #             "credentials.json",
# #             scopes=SCOPES,
# #             redirect_uri=REDIRECT_URI  # ✅ Set it only here
# #         )

# #         creds = flow.run_local_server(port=5500, redirect_uri_trusted=True)

# #         with open(token_path, "w") as token:
# #             token.write(creds.to_json())

# #     # Calendar API service
# #     service = build("calendar", "v3", credentials=creds)

# #     # Define event
# #     event = {
# #         "summary": f"📘 Finish StudyGenie Roadmap: {user_email}",
# #         "description": roadmap_text[:1000],  # Shorten description to be safe
# #         "start": {"date": start_time.strftime("%Y-%m-%d")},
# #         "end": {"date": end_time.strftime("%Y-%m-%d")},
# #     }

# #     service.events().insert(calendarId="primary", body=event).execute()

# import datetime
# import os.path
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build

# SCOPES = ["https://www.googleapis.com/auth/calendar"]

# def add_to_calendar(user_email, roadmap_text, deadline_str):
#     # Format deadline
#     deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d")
#     start_time = deadline - datetime.timedelta(days=7)
#     end_time = deadline

#     creds = None
#     token_path = "backend/token.json"

#     if os.path.exists(token_path):
#         creds = Credentials.from_authorized_user_file(token_path, SCOPES)
#     else:
#         # Create flow WITHOUT redirect_uri (default is http://localhost:5500/)
#         flow = InstalledAppFlow.from_client_secrets_file(
#             "credentials.json",  # Ensure this path is correct
#             scopes=SCOPES
#         )
#         creds = flow.run_local_server(port=5500)  # Default redirect used here

#         # Save credentials for reuse
#         with open(token_path, "w") as token:
#             token.write(creds.to_json())

#     # Calendar API service
#     service = build("calendar", "v3", credentials=creds)

#     # Define event
#     event = {
#         "summary": f"📘 Finish StudyGenie Roadmap: {user_email}",
#         "description": roadmap_text[:1000],  # Shorten to avoid API limit
#         "start": {"date": start_time.strftime("%Y-%m-%d")},
#         "end": {"date": end_time.strftime("%Y-%m-%d")},
#     }

#     service.events().insert(calendarId="primary", body=event).execute()



import datetime
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def add_to_calendar(user_email, roadmap_text, deadline_str):
    # Format deadline
    deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d")
    start_time = deadline - datetime.timedelta(days=7)
    end_time = deadline

    creds = None
    token_path = "backend/token.json"

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("backend/credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open(token_path, "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)

    event = {
        "summary": f"📘 Finish StudyGenie Roadmap: {user_email}",
        "description": roadmap_text[:1000],  # Shorten for safety
        "start": {"date": start_time.strftime("%Y-%m-%d")},
        "end": {"date": end_time.strftime("%Y-%m-%d")},
    }

    service.events().insert(calendarId="primary", body=event).execute()
