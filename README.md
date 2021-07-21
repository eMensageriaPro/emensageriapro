# eMensageriaPro

# VERSÃO DESATUALIZADA ACESSE O REPOSITÓRIO: https://github.com/marcelomdevasconcellos/emensageria/

eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>

Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

## Versões compatíveis do eSocial

- 2.04.02
- 2.05.00 (até NT 18/2020)
- NDE 02/2018 - EVENTOS RELATIVOS A ÓRGÃOS/ENTES DO PODER PÚBLICO

## Versões compatíveis do EFD-Reinf

- 1.03.02
- 1.04.00

## Requisitos de Sistema

- Python (versão 2.7);
- Django (versão 1.11.28);
- Postgres 9.6;

## Instalação usando docker:

__Autor:__ Marcos Roberto <marcosroberto1808@gmail.com>

__Starting all services in detached mode:__

`docker-compose up -d`

__Execute initial migrate:__

`docker-compose exec app python migrate_all_apps.py`

## Atualização de Banco de dados:

`python migrate_all_apps.py`

## Licença AGPL-3

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Contato

Marcelo Medeiros de Vasconcellos <marcelomdevasconcellos@gmail.com>

Para maiores informações acesse: www.emensageria.com.br e baixe o Manual de Instruções


