# eMensageriaPro

eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

## Requisitos de Sistema

- Linux;
- Python (versão 2.7);
- Django (versão 1.11.15);
- Postgres 9.6;

# Instalação usando docker:

Contribuição Marcos Roberto <marcosroberto1808@gmail.com>

## Starting all services in detached mode:
`docker-compose up -d`

## Execute initial migrate
`docker-compose exec app python migrate_all_apps.py`

## Atualização de Banco de dados:

`python migrate_all_apps.py`

# Versão de Demostração:

https://www.emensageria.com.br/index.php?page=demo#demo
- login: admin
- senha: admin

# Licença AGPL-3

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

  Este programa é software livre: você pode redistribuí-lo e/ou modificá-lo
  sob os termos da licença GNU Affero General Public License como
  publicado pela Free Software Foundation, seja versão 3 do
  Licença, ou (a seu critério) qualquer versão posterior.

  Este programa é distribuído na esperança de que seja útil,
  mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
  COMERCIABILIDADE ou ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
  Licença Pública Geral GNU Affero para mais detalhes.

  Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
  junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

  Para maiores informações acesse: www.emensageria.com.br e baixe o Manual de Instruções

# Contato

Marcelo Medeiros de Vasconcellos
contato@emensageria.com.br

