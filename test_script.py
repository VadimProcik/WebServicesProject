import requests

# Function to check if a specific word exists in the response content
def check_service_for_word(url, keyword):
    try:
        response = requests.get(url)
        if keyword in response.text:
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return False

# Function to save test results to a file
def save_result(name, url, result):
    with open('test.log', 'a') as f:
        f.write(f'Test name: {name}\n')
        f.write(f'Test URL: {url}\n')
        f.write(f'Test result: {result}\n')
        f.write('---------------------------------------------\n')

if __name__ == "__main__":
    # Test 1
    name = 'Test 1'
    url = 'http://localhost:5000/getProducts'
    keyword = 'id'
    result = check_service_for_word(url, keyword)
    save_result(name, url, result)

    # Test 2
    name = 'Test 2'
    url = 'http://localhost:5000/getTitles'
    keyword = 'jacket'
    result = check_service_for_word(url, keyword)
    save_result(name, url, result)
