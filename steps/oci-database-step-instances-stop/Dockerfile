FROM relaysh/core:latest-python
RUN apk --no-cache add gcc musl-dev libffi-dev openssl-dev
RUN pip install oci
COPY "./step.py" "/nebula/step-compute-stop-instances.py"
COPY "./.oci/*" "/root/.oci/"
ENTRYPOINT []
CMD ["python3", "/nebula/step-compute-stop-instances.py"]

LABEL "org.opencontainers.image.title"="Stop OCI Compute instances"
LABEL "org.opencontainers.image.description"="This task stops a given list of OCI Compute instances."
LABEL "com.puppet.nebula.sdk.version"="v1"
