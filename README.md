# eMensageriaPro

eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>

Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

## Requisitos de Sistema

- Python (versão 2.7);
- Django (versão 1.11.15);
- Postgres 9.6;

## Instalação usando docker:

__Autor:__ Marcos Roberto <marcosroberto1808@gmail.com>

__Starting all services in detached mode:__

`docker-compose up -d`

__Execute initial migrate:__

`docker-compose exec app python migrate_all_apps.py`

## Atualização de Banco de dados:

`python migrate_all_apps.py`

## Versão de Demostração:

__https://www.emensageria.com.br/index.php?page=demo#demo__
- login: admin
- senha: admin

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


