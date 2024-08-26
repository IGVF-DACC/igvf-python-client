# AI Generated
import re


def parse_and_reorder_readme():
    # Read the README.md file
    with open('README.md', 'r') as file:
        content = file.read()

    # Extract the API Endpoints section
    api_endpoints_match = re.search(r'## Documentation for API Endpoints\n\n(.+?)\n\n## Documentation For Models', content, re.DOTALL)
    if not api_endpoints_match:
        print("API Endpoints section not found")
        return

    api_endpoints = api_endpoints_match.group(1)

    # Split the endpoints into lines, preserving the header
    endpoint_lines = api_endpoints.strip().split('\n')
    header_lines = endpoint_lines[:4]  # Preserve the header lines
    endpoint_lines = endpoint_lines[4:]  # The rest are the actual endpoints

    # Separate main API endpoints and collection endpoints
    main_endpoints = []
    collection_endpoints = []

    for line in endpoint_lines:
        if '@@listing' in line:
            collection_endpoints.append(line)
        else:
            main_endpoints.append(line)

    # Sort the lists alphabetically
    main_endpoints.sort(reverse=True)
    collection_endpoints.sort()

    # Move 'search' and 'get_by_id' to the top of main_endpoints
    for endpoint in ['search', 'get_by_id']:
        for line in main_endpoints:
            if f'*IgvfApi* | [**{endpoint}**]' in line:
                main_endpoints.remove(line)
                main_endpoints.insert(0, line)
                break

    # Combine the sorted lists with headers
    new_api_endpoints = ("### **General Endpoints**\n\n"
                         f"{chr(10).join(header_lines)}\n"
                         f"{chr(10).join(main_endpoints)}\n"
                         "\n"
                         "### **Collection Endpoints**\n\n"
                         f"{chr(10).join(header_lines)}\n"
                         f"{chr(10).join(collection_endpoints)}")

    # Replace the old API Endpoints section with the new one
    new_content = re.sub(r'## Documentation for API Endpoints\n\n.+?\n\n## Documentation For Models',
                         f'## Documentation for API Endpoints\n\n{new_api_endpoints}\n\n## Documentation For Models',
                         content, flags=re.DOTALL)

    # Write the modified content back to README.md
    with open('README.md', 'w') as file:
        file.write(new_content)

    print("README.md has been successfully updated.")

# Run the function
parse_and_reorder_readme()
