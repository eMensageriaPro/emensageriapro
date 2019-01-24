# Dockerfile by Marcos Roberto
FROM postgres:9.6
LABEL author="marcosroberto1808@gmail.com"
# Fix container timezone
ENV TZ=America/Fortaleza
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# Fix postgres locale
RUN localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
ENV LANG="pt_BR.UTF-8"

# Add initial SQL scripts to run on first postgres start up.
ADD ./sql_scripts/. /docker-entrypoint-initdb.d