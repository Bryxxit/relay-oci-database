FROM relaysh/core:latest-python
RUN apk --no-cache add gcc musl-dev libffi-dev openssl-dev
RUN pip install oci
COPY "./step.py" "/nebula/step-database-describe-versions.py"
COPY "./.oci/*" "/root/.oci/"
ENTRYPOINT []
CMD ["python3", "/nebula/step-database-describe-versions.py"]

LABEL "org.opencontainers.image.title"="Describe OCI database versions"
LABEL "org.opencontainers.image.description"="This task describes the database versions in a given region."
LABEL "com.puppet.nebula.sdk.version"="v1"
