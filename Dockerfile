FROM node:latest as node

RUN apt-get https://github.com/Spiritdude/Cura-CLI-Wrapper

COPY app /app

RUN npm install cura-cli 

FROM freesurfer/freesurfer:7.1.1

COPY license /usr/local/freesurfer/.license
COPY --from=node /app /app

CMD ["main.py"]