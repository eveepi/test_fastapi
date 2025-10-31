FROM mcr.microsoft.com/devcontainers/python:2-3.12-bullseye AS dev

# Allow user to install packages globally
ENV PIP_TARGET=/usr/local/pip-global
ENV PYTHONPATH=${PIP_TARGET}:${PYTHON_PATH}
ENV PATH=${PIP_TARGET}/bin:${PATH}
RUN if ! cat /etc/group | grep -e "^pip-global:" > /dev/null 2>&1; then groupadd -r pip-global; fi \
    && usermod -a -G pip-global vscode \
    && umask 0002 && mkdir -p ${PIP_TARGET} \
    && chown :pip-global ${PIP_TARGET} \
    && ( [ ! -f "/etc/profile.d/00-restore-env.sh" ] || sed -i -e "s/export PATH=/export PATH=\/usr\/local\/pip-global:/" /etc/profile.d/00-restore-env.sh )


# Install deps from pyproject.toml
COPY ./src/pyproject.toml /app/src/pyproject.toml

RUN python -m pip install uv \
    && uv pip install -r /app/src/pyproject.toml --all-extras --target ${PIP_TARGET}

COPY ./src /app/src

WORKDIR "/app"

CMD ["python", "-m", "src.api_v1.main"]
