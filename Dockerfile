FROM python:3.11-alpine

RUN mkdir /apps
WORKDIR /apps
COPY . .
RUN ls
CMD python
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r req.txt

RUN sed -i 's/\r$//g' /apps/entrypoint.sh
RUN chmod +x /apps/entrypoint.sh

ENTRYPOINT ["/apps/entrypoint.sh"]