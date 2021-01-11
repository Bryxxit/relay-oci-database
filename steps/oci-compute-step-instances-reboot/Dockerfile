FROM relaysh/core:latest-python
RUN apk --no-cache add gcc musl-dev libffi-dev openssl-dev
RUN pip install oci
COPY "./step.py" "/nebula/step-compute-reboot-instances.py"
COPY "./.oci/*" "/root/.oci/"
ENTRYPOINT []
CMD ["python3", "/nebula/step-compute-reboot-instances.py"]

LABEL "org.opencontainers.image.title"="Reboot OCI compute instances"
LABEL "org.opencontainers.image.description"="This task reboots the compute instances in a given region."
LABEL "com.puppet.nebula.sdk.version"="v1"
