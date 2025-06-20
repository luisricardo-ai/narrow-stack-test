FROM mageai/mageai:latest
WORKDIR /home/src
CMD ["mage", "start", "mage_data"]