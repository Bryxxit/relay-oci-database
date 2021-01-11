FROM relaysh/core:latest-python
RUN apk --no-cache add gcc musl-dev libffi-dev openssl-dev
RUN pip install oci
COPY "./step.py" "/nebula/step-compute-describe-images.py"
COPY "./.oci/*" "/root/.oci/"
ENTRYPOINT []
CMD ["python3", "/nebula/step-compute-describe-images.py"]

LABEL "org.opencontainers.image.title"="Describe OCI compute images"
LABEL "org.opencontainers.image.description"="This task describes the compute images in a given region."
LABEL "com.puppet.nebula.sdk.version"="v1"
