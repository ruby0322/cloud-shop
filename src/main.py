import sys

from src.services.marketplace_service import MarketplaceService


def parse_command(line: str):
    """Parse command line input, handling quoted strings properly"""
    parts = []
    current = []
    in_quotes = False
    
    for char in line:
        if char == "'" and not in_quotes:
            in_quotes = True
        elif char == "'" and in_quotes:
            in_quotes = False
            if current:
                parts.append(''.join(current))
                current = []
        elif char.isspace() and not in_quotes:
            if current:
                parts.append(''.join(current))
                current = []
        else:
            current.append(char)
            
    if current:
        parts.append(''.join(current))
        
    return parts

def main():
    marketplace = MarketplaceService()
    
    while True:
        try:
            # Print prompt
            print("# ", end="", flush=True)
            
            # Read input
            line = input().strip()
            if not line:
                continue
                
            # Parse command
            parts = parse_command(line)
            if not parts:
                continue
                
            command = parts[0].upper()
            
            # Process commands
            if command == "REGISTER" and len(parts) == 2:
                print(marketplace.register_user(parts[1]))
                
            elif command == "CREATE_LISTING" and len(parts) == 6:
                print(marketplace.create_listing(
                    parts[1],  # username
                    parts[2],  # title
                    parts[3],  # description
                    float(parts[4]),  # price
                    parts[5]   # category
                ))
                
            elif command == "DELETE_LISTING" and len(parts) == 3:
                print(marketplace.delete_listing(
                    parts[1],  # username
                    int(parts[2])  # listing_id
                ))
                
            elif command == "GET_LISTING" and len(parts) == 3:
                print(marketplace.get_listing(
                    parts[1],  # username
                    int(parts[2])  # listing_id
                ))
                
            elif command == "GET_CATEGORY" and len(parts) == 3:
                print(marketplace.get_category(
                    parts[1],  # username
                    parts[2]   # category
                ))
                
            elif command == "GET_TOP_CATEGORY" and len(parts) == 2:
                print(marketplace.get_top_category(parts[1]))
                
            else:
                print("Error - invalid command or arguments")
                
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        except ValueError as e:
            print("Error - invalid number format")
        except Exception as e:
            sys.stdout.write(e)

if __name__ == "__main__":
    main() 