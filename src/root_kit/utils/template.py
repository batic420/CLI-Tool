from jinja2 import Template

template = Template("""
services:
  mysql-{{ custom_key }}:
    image: mysql:8.0      
    container_name: rootkit-mysql
    ports:
      - "${MYSQL_PORT}:3306"       
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}   
      MYSQL_DATABASE: ${MYSQL_DATABASE}           
      MYSQL_USER: ${MYSQL_USER}    
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}         
    volumes:
      - mysql_data:/var/lib/mysql    # Persist data even if the container restarts
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 5s
      timeout: 10s
      retries: 5

volumes:
  mysql_data:
""")

def generate_template(
        custom_key: str,
        file_path: str
):
    f = open(file_path, "w")

    if f:
        f.write(template.render(custom_key=custom_key))
        f.close()