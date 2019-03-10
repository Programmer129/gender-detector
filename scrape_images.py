

from google_images_download import google_images_download

arguments = {"keywords": "man and woman pictures couple", "limit": 100, "print_urls": True, "output_directory": "/home/avto/Desktop"}
response = google_images_download.googleimagesdownload()
absolute_image_paths = response.download(arguments=arguments)
