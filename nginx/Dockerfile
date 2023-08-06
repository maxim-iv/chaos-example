FROM fabiocicerchia/nginx-lua

# Copy Nginx configuration file to the container
RUN rm /etc/nginx/conf.d/default.conf
COPY conf.d/nginx.conf /etc/nginx/conf.d

# Expose port 80
EXPOSE 80
