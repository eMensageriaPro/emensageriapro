#coding:utf-8


"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

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

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.
    
        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""


import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo


def validacoes_s2240_evtexprisco(arquivo):

    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtExpRisco = doc.eSocial.evtExpRisco
    #variaveis
    
    if 'ideEvento' in dir(evtExpRisco.ideEvento):
        for ideEvento in evtExpRisco.ideEvento:
            
            if 'indRetif' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.indRetif', 
                                                  ideEvento.indRetif.cdata, 
                                                  1, u'1, 2')
            
            if 'nrRecibo' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.nrRecibo', 
                                                  ideEvento.nrRecibo.cdata, 
                                                  0, u'None')
            
            if 'tpAmb' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.tpAmb', 
                                                  ideEvento.tpAmb.cdata, 
                                                  1, u'1, 2')
            
            if 'procEmi' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.procEmi', 
                                                  ideEvento.procEmi.cdata, 
                                                  1, u'1, 2, 3, 4, 5')
            
            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc', 
                                                  ideEvento.verProc.cdata, 
                                                  1, u'None')
    
    if 'ideEmpregador' in dir(evtExpRisco.ideEmpregador):
        for ideEmpregador in evtExpRisco.ideEmpregador:
            
            if 'tpInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.tpInsc', 
                                                  ideEmpregador.tpInsc.cdata, 
                                                  1, u'1, 2, 3, 4, 5')
            
            if 'nrInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.nrInsc', 
                                                  ideEmpregador.nrInsc.cdata, 
                                                  1, u'None')
    
    if 'ideVinculo' in dir(evtExpRisco.ideVinculo):
        for ideVinculo in evtExpRisco.ideVinculo:
            
            if 'cpfTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.cpfTrab', 
                                                  ideVinculo.cpfTrab.cdata, 
                                                  1, u'None')
            
            if 'nisTrab' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.nisTrab', 
                                                  ideVinculo.nisTrab.cdata, 
                                                  0, u'None')
            
            if 'matricula' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.matricula', 
                                                  ideVinculo.matricula.cdata, 
                                                  0, u'None')
            
            if 'codCateg' in dir(ideVinculo):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideVinculo.codCateg', 
                                                  ideVinculo.codCateg.cdata, 
                                                  0, u'101, 102, 103, 104, 105, 106, 111, 201, 202, 301, 302, 303, 305, 306, 307, 308, 309, 401, 410, 701, 711, 712, 721, 722, 723, 731, 734, 738, 741, 751, 761, 771, 781, 901, 902, 903, 904, 905')
    
    if 'infoExpRisco' in dir(evtExpRisco.infoExpRisco):
        for infoExpRisco in evtExpRisco.infoExpRisco:
            
            if 'dtIniCondicao' in dir(infoExpRisco):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'infoExpRisco.dtIniCondicao', 
                                                  infoExpRisco.dtIniCondicao.cdata, 
                                                  1, u'None')
            
            if 'infoAmb' in dir(infoExpRisco.infoAmb):
                for infoAmb in infoExpRisco.infoAmb:
                    
                    if 'codAmb' in dir(infoAmb):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoAmb.codAmb', 
                                                          infoAmb.codAmb.cdata, 
                                                          1, u'None')
            
            if 'infoAtiv' in dir(infoExpRisco.infoAtiv):
                for infoAtiv in infoExpRisco.infoAtiv:
                    
                    if 'dscAtivDes' in dir(infoAtiv):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'infoAtiv.dscAtivDes', 
                                                          infoAtiv.dscAtivDes.cdata, 
                                                          1, u'None')
                    
                    if 'ativPericInsal' in dir(infoAtiv.ativPericInsal):
                        for ativPericInsal in infoAtiv.ativPericInsal:
                            
                            if 'codAtiv' in dir(ativPericInsal):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ativPericInsal.codAtiv', 
                                                                  ativPericInsal.codAtiv.cdata, 
                                                                  1, u'01.001, 01.002, 01.003, 01.004, 01.005, 01.006, 01.007, 01.008, 01.009, 01.010, 01.011, 01.012, 01.013, 01.014, 02.001, 02.002, 02.003, 02.004, 02.005, 02.006, 02.007, 02.008, 02.009, 02.010, 02.011, 02.012, 02.013, 02.014, 02.015, 02.016, 02.017, 02.018, 02.019, 02.020, 02.021, 02.022, 02.023, 02.024, 02.025, 02.026, 02.027, 02.028, 02.029, 02.030, 02.031, 02.032, 02.033, 02.034, 02.035, 02.036, 02.037, 02.038, 02.039, 02.040, 02.041, 02.042, 02.043, 02.044, 02.045, 02.046, 02.047, 02.048, 02.049, 02.050, 02.051, 02.052, 02.053, 02.054, 02.055, 02.056, 02.057, 02.058, 02.059, 02.060, 02.061, 02.062, 02.063, 02.064, 02.065, 02.066, 02.067, 02.068, 02.069, 02.070, 02.071, 02.072, 02.073, 02.074, 02.075, 02.076, 02.077, 02.078, 02.079, 02.080, 02.081, 02.082, 02.083, 02.084, 02.085, 02.086, 02.087, 02.088, 02.089, 02.090, 02.091, 02.092, 02.093, 02.094, 02.095, 02.096, 02.097, 02.098, 02.099, 02.100, 02.101, 02.102, 03.001, 03.002, 03.003, 03.004, 03.005, 03.006, 03.007, 03.008, 04.001, 04.002, 04.003, 04.004, 04.005, 04.006, 04.007, 04.008, 04.009, 04.010, 04.011, 04.012, 04.013, 04.014, 04.015, 04.016, 04.017, 04.018, 04.019, 04.020, 04.021, 04.022, 04.023, 04.024, 04.025, 04.026, 04.027, 04.028, 04.029, 04.030, 04.031, 05.001, 05.002, 05.003, 05.004, 05.005, 05.006, 05.007, 05.008, 05.009, 05.010, 05.011, 06.001, 06.002, 06.003, 06.004, 06.005, 06.006, 06.007, 06.008, 06.009, 07.001, 07.002, 07.003, 07.004, 07.005, 07.006, 07.007, 08.001, 09.001, 09.002, 09.003, 09.004, 09.005, 09.006, 09.007, 09.008, 09.009, 09.010, 09.011, 10.001, 10.002, 10.003, 10.005, 10.006, 10.007, 10.008, 10.009, 11.001, 11.002, 99.999')
            
            if 'fatRisco' in dir(infoExpRisco.fatRisco):
                for fatRisco in infoExpRisco.fatRisco:
                    
                    if 'codFatRis' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.codFatRis', 
                                                          fatRisco.codFatRis.cdata, 
                                                          1, u'01.01.01, 01.01.02, 01.01.03, 01.01.04, 01.01.05, 01.01.06, 01.01.07, 01.01.08, 01.01.09, 01.01.10, 01.01.11, 01.01.12, 01.01.13, 01.01.14, 01.01.15, 01.01.16, 01.01.17, 01.01.18, 01.01.19, 01.01.20, 01.01.21, 01.01.22, 01.01.23, 0.101.999, 02.01.01, 02.01.02, 02.01.03, 02.01.04, 02.01.05, 02.01.06, 02.01.07, 02.01.08, 02.01.09, 02.01.10, 02.01.11, 02.01.12, 02.01.13, 02.01.14, 02.01.15, 02.01.16, 02.01.17, 02.01.18, 02.01.19, 02.01.20, 02.01.21, 02.01.22, 02.01.23, 02.01.24, 02.01.25, 02.01.26, 02.01.27, 02.01.28, 02.01.29, 02.01.30, 02.01.31, 02.01.32, 02.01.33, 02.01.34, 02.01.35, 02.01.36, 02.01.37, 02.01.38, 02.01.39, 02.01.40, 02.01.41, 02.01.42, 02.01.43, 02.01.44, 02.01.45, 02.01.46, 02.01.47, 02.01.48, 02.01.49, 02.01.50, 02.01.51, 02.01.52, 02.01.53, 02.01.54, 02.01.55, 02.01.56, 02.01.57, 02.01.59, 02.01.60, 02.01.61, 02.01.62, 02.01.63, 02.01.64, 02.01.65, 02.01.66, 02.01.67, 02.01.68, 02.01.69, 02.01.70, 02.01.71, 02.01.72, 02.01.73, 02.01.74, 02.01.75, 02.01.76, 02.01.77, 02.01.78, 02.01.79, 02.01.80, 02.01.81, 02.01.82, 02.01.83, 02.01.84, 02.01.86, 02.01.87, 02.01.88, 02.01.89, 02.01.90, 02.01.91, 02.01.92, 02.01.93, 02.01.94, 02.01.95, 02.01.96, 02.01.97, 02.01.98, 02.01.99, 0.201.100, 0.201.101, 0.201.102, 0.201.103, 0.201.104, 0.201.105, 0.201.106, 0.201.107, 0.201.108, 0.201.109, 0.201.110, 0.201.111, 0.201.112, 0.201.113, 0.201.114, 0.201.115, 0.201.116, 0.201.117, 0.201.118, 0.201.119, 0.201.121, 0.201.122, 0.201.123, 0.201.124, 0.201.125, 0.201.126, 0.201.127, 0.201.128, 0.201.130, 0.201.131, 0.201.132, 0.201.133, 0.201.135, 0.201.136, 0.201.137, 0.201.138, 0.201.139, 0.201.140, 0.201.141, 0.201.143, 0.201.144, 0.201.145, 0.201.146, 0.201.147, 0.201.148, 0.201.149, 0.201.150, 0.201.151, 0.201.152, 0.201.153, 0.201.154, 0.201.155, 0.201.156, 0.201.157, 0.201.158, 0.201.159, 0.201.160, 0.201.161, 0.201.162, 0.201.163, 0.201.164, 0.201.165, 0.201.166, 0.201.167, 0.201.169, 0.201.170, 0.201.171, 0.201.172, 0.201.173, 0.201.174, 0.201.175, 0.201.176, 0.201.177, 0.201.178, 0.201.179, 0.201.180, 0.201.181, 0.201.182, 0.201.183, 0.201.184, 0.201.185, 0.201.186, 0.201.187, 0.201.188, 0.201.189, 0.201.190, 0.201.191, 0.201.192, 0.201.193, 0.201.194, 0.201.195, 0.201.196, 0.201.197, 0.201.198, 0.201.200, 0.201.201, 0.201.202, 0.201.203, 0.201.204, 0.201.205, 0.201.206, 0.201.207, 0.201.208, 0.201.209, 0.201.210, 0.201.212, 0.201.213, 0.201.214, 0.201.215, 0.201.216, 0.201.217, 0.201.219, 0.201.220, 0.201.223, 0.201.224, 0.201.225, 0.201.226, 0.201.227, 0.201.228, 0.201.229, 0.201.230, 0.201.231, 0.201.232, 0.201.233, 0.201.234, 0.201.235, 0.201.236, 0.201.237, 0.201.238, 0.201.239, 0.201.240, 0.201.241, 0.201.242, 0.201.243, 0.201.244, 0.201.245, 0.201.246, 0.201.247, 0.201.248, 0.201.249, 0.201.250, 0.201.251, 0.201.252, 0.201.253, 0.201.254, 0.201.255, 0.201.257, 0.201.258, 0.201.259, 0.201.260, 0.201.261, 0.201.262, 0.201.263, 0.201.264, 0.201.265, 0.201.266, 0.201.267, 0.201.268, 0.201.269, 0.201.270, 0.201.271, 0.201.272, 0.201.273, 0.201.274, 0.201.275, 0.201.276, 0.201.277, 0.201.278, 0.201.279, 0.201.280, 0.201.281, 0.201.282, 0.201.283, 0.201.284, 0.201.285, 0.201.286, 0.201.287, 0.201.288, 0.201.289, 0.201.290, 0.201.291, 0.201.292, 0.201.293, 0.201.294, 0.201.295, 0.201.296, 0.201.297, 0.201.298, 0.201.299, 0.201.300, 0.201.301, 0.201.302, 0.201.304, 0.201.305, 0.201.306, 0.201.307, 0.201.308, 0.201.309, 0.201.310, 0.201.311, 0.201.312, 0.201.313, 0.201.314, 0.201.315, 0.201.316, 0.201.317, 0.201.318, 0.201.319, 0.201.320, 0.201.321, 0.201.322, 0.201.323, 0.201.324, 0.201.325, 0.201.326, 0.201.327, 0.201.328, 0.201.329, 0.201.330, 0.201.331, 0.201.332, 0.201.333, 0.201.334, 0.201.335, 0.201.336, 0.201.337, 0.201.338, 0.201.339, 0.201.340, 0.201.341, 0.201.342, 0.201.343, 0.201.344, 0.201.345, 0.201.346, 0.201.347, 0.201.348, 0.201.349, 0.201.352, 0.201.353, 0.201.354, 0.201.355, 0.201.356, 0.201.357, 0.201.358, 0.201.359, 0.201.360, 0.201.362, 0.201.363, 0.201.365, 0.201.366, 0.201.367, 0.201.368, 0.201.369, 0.201.370, 0.201.371, 0.201.372, 0.201.373, 0.201.374, 0.201.375, 0.201.376, 0.201.377, 0.201.378, 0.201.380, 0.201.381, 0.201.382, 0.201.383, 0.201.384, 0.201.385, 0.201.386, 0.201.387, 0.201.388, 0.201.389, 0.201.390, 0.201.391, 0.201.392, 0.201.393, 0.201.394, 0.201.395, 0.201.396, 0.201.397, 0.201.398, 0.201.399, 0.201.400, 0.201.401, 0.201.402, 0.201.403, 0.201.404, 0.201.405, 0.201.406, 0.201.407, 0.201.408, 0.201.409, 0.201.410, 0.201.411, 0.201.412, 0.201.413, 0.201.414, 0.201.416, 0.201.417, 0.201.418, 0.201.419, 0.201.420, 0.201.421, 0.201.422, 0.201.423, 0.201.424, 0.201.425, 0.201.426, 0.201.427, 0.201.428, 0.201.429, 0.201.430, 0.201.431, 0.201.432, 0.201.433, 0.201.434, 0.201.435, 0.201.436, 0.201.438, 0.201.440, 0.201.441, 0.201.442, 0.201.445, 0.201.446, 0.201.447, 0.201.448, 0.201.449, 0.201.450, 0.201.451, 0.201.452, 0.201.453, 0.201.455, 0.201.457, 0.201.458, 0.201.459, 0.201.460, 0.201.461, 0.201.462, 0.201.463, 0.201.464, 0.201.465, 0.201.466, 0.201.467, 0.201.468, 0.201.469, 0.201.470, 0.201.471, 0.201.472, 0.201.473, 0.201.474, 0.201.475, 0.201.476, 0.201.477, 0.201.478, 0.201.479, 0.201.480, 0.201.481, 0.201.482, 0.201.483, 0.201.484, 0.201.485, 0.201.486, 0.201.487, 0.201.488, 0.201.489, 0.201.490, 0.201.491, 0.201.492, 0.201.493, 0.201.494, 0.201.495, 0.201.497, 0.201.498, 0.201.499, 0.201.500, 0.201.501, 0.201.502, 0.201.503, 0.201.505, 0.201.506, 0.201.507, 0.201.508, 0.201.509, 0.201.510, 0.201.511, 0.201.512, 0.201.513, 0.201.514, 0.201.515, 0.201.518, 0.201.519, 0.201.520, 0.201.521, 0.201.522, 0.201.523, 0.201.524, 0.201.525, 0.201.526, 0.201.527, 0.201.528, 0.201.529, 0.201.530, 0.201.531, 0.201.532, 0.201.533, 0.201.534, 0.201.535, 0.201.536, 0.201.537, 0.201.539, 0.201.540, 0.201.541, 0.201.542, 0.201.543, 0.201.544, 0.201.545, 0.201.546, 0.201.547, 0.201.548, 0.201.549, 0.201.550, 0.201.552, 0.201.553, 0.201.555, 0.201.556, 0.201.557, 0.201.558, 0.201.559, 0.201.560, 0.201.561, 0.201.562, 0.201.563, 0.201.564, 0.201.565, 0.201.566, 0.201.567, 0.201.568, 0.201.569, 0.201.570, 0.201.571, 0.201.572, 0.201.573, 0.201.574, 0.201.575, 0.201.576, 0.201.577, 0.201.578, 0.201.579, 0.201.580, 0.201.581, 0.201.583, 0.201.584, 0.201.585, 0.201.586, 0.201.587, 0.201.588, 0.201.589, 0.201.590, 0.201.591, 0.201.592, 0.201.593, 0.201.594, 0.201.595, 0.201.596, 0.201.597, 0.201.598, 0.201.599, 0.201.600, 0.201.601, 0.201.602, 0.201.603, 0.201.604, 0.201.605, 0.201.606, 0.201.607, 0.201.608, 0.201.609, 0.201.610, 0.201.611, 0.201.612, 0.201.613, 0.201.614, 0.201.615, 0.201.616, 0.201.617, 0.201.618, 0.201.619, 0.201.620, 0.201.621, 0.201.622, 0.201.623, 0.201.624, 0.201.625, 0.201.626, 0.201.627, 0.201.628, 0.201.629, 0.201.630, 0.201.631, 0.201.632, 0.201.633, 0.201.634, 0.201.635, 0.201.636, 0.201.637, 0.201.638, 0.201.639, 0.201.640, 0.201.641, 0.201.642, 0.201.643, 0.201.644, 0.201.645, 0.201.646, 0.201.648, 0.201.649, 0.201.650, 0.201.651, 0.201.652, 0.201.653, 0.201.654, 0.201.655, 0.201.657, 0.201.658, 0.201.659, 0.201.661, 0.201.662, 0.201.664, 0.201.665, 0.201.666, 0.201.667, 0.201.668, 0.201.670, 0.201.671, 0.201.672, 0.201.673, 0.201.674, 0.201.675, 0.201.676, 0.201.677, 0.201.678, 0.201.679, 0.201.680, 0.201.681, 0.201.682, 0.201.683, 0.201.684, 0.201.685, 0.201.686, 0.201.687, 0.201.688, 0.201.689, 0.201.690, 0.201.691, 0.201.692, 0.201.693, 0.201.694, 0.201.695, 0.201.696, 0.201.697, 0.201.698, 0.201.699, 0.201.700, 0.201.701, 0.201.702, 0.201.703, 0.201.704, 0.201.705, 0.201.706, 0.201.707, 0.201.708, 0.201.709, 0.201.710, 0.201.711, 0.201.712, 0.201.713, 0.201.714, 0.201.715, 0.201.716, 0.201.717, 0.201.718, 0.201.719, 0.201.720, 0.201.721, 0.201.722, 0.201.723, 0.201.724, 0.201.725, 0.201.726, 0.201.727, 0.201.728, 0.201.729, 0.201.730, 0.201.731, 0.201.732, 0.201.733, 0.201.734, 0.201.735, 0.201.736, 0.201.737, 0.201.738, 0.201.739, 0.201.740, 0.201.741, 0.201.742, 0.201.743, 0.201.744, 0.201.745, 0.201.746, 0.201.747, 0.201.748, 0.201.749, 0.201.750, 0.201.751, 0.201.752, 0.201.753, 0.201.754, 0.201.755, 0.201.756, 0.201.758, 0.201.759, 0.201.760, 0.201.761, 0.201.762, 0.201.763, 0.201.764, 0.201.765, 0.201.767, 0.201.768, 0.201.769, 0.201.770, 0.201.771, 0.201.772, 0.201.773, 0.201.774, 0.201.775, 0.201.776, 0.201.777, 0.201.778, 0.201.779, 0.201.780, 0.201.781, 0.201.782, 0.201.783, 0.201.785, 0.201.786, 0.201.787, 0.201.788, 0.201.789, 0.201.999, 03.01.01, 0.301.999, 04.01.01, 04.01.02, 04.01.03, 04.01.04, 04.01.05, 04.01.06, 04.01.07, 04.01.08, 04.01.09, 04.01.10, 04.01.11, 04.01.12, 04.01.13, 04.01.14, 04.01.15, 04.01.16, 04.01.17, 04.01.18, 04.01.19, 04.01.20, 0.401.999, 04.02.01, 04.02.02, 04.02.03, 04.02.04, 04.02.05, 04.02.06, 04.02.07, 04.02.08, 04.02.09, 0.402.999, 04.03.01, 04.03.02, 04.03.03, 04.03.04, 04.03.05, 04.03.06, 04.03.07, 04.03.08, 04.03.09, 04.03.10, 0.403.999, 04.04.01, 04.04.02, 04.04.03, 04.04.04, 04.04.05, 04.04.06, 04.04.07, 04.04.08, 0.404.999, 04.05.01, 04.05.02, 04.05.03, 04.05.04, 04.05.05, 04.05.06, 04.05.07, 04.05.08, 04.05.09, 04.05.10, 04.05.11, 0.405.999, 05.01.01, 05.01.02, 05.01.03, 05.01.04, 05.01.05, 05.01.06, 05.01.07, 05.01.08, 05.01.09, 05.01.10, 05.01.11, 05.01.12, 05.01.13, 05.01.14, 05.01.15, 05.01.16, 05.01.17, 05.01.18, 05.01.19, 05.01.20, 05.01.21, 05.01.22, 05.01.23, 05.01.24, 05.01.25, 05.01.26, 05.01.27, 05.01.28, 05.01.29, 05.01.30, 05.01.31, 05.01.32, 0.501.999, 06.01.01, 07.01.01, 08.01.01, 09.01.01')
                    
                    if 'tpAval' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.tpAval', 
                                                          fatRisco.tpAval.cdata, 
                                                          1, u'1, 2')
                    
                    if 'intConc' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.intConc', 
                                                          fatRisco.intConc.cdata, 
                                                          0, u'None')
                    
                    if 'limTol' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.limTol', 
                                                          fatRisco.limTol.cdata, 
                                                          0, u'None')
                    
                    if 'unMed' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.unMed', 
                                                          fatRisco.unMed.cdata, 
                                                          0, u'1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 26, 27, 28, 29, 30, 31, 32, 35, 36, 37, 39, 43')
                    
                    if 'tecMedicao' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.tecMedicao', 
                                                          fatRisco.tecMedicao.cdata, 
                                                          0, u'None')
                    
                    if 'insalubridade' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.insalubridade', 
                                                          fatRisco.insalubridade.cdata, 
                                                          0, u'S, N')
                    
                    if 'periculosidade' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.periculosidade', 
                                                          fatRisco.periculosidade.cdata, 
                                                          0, u'S, N')
                    
                    if 'aposentEsp' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.aposentEsp', 
                                                          fatRisco.aposentEsp.cdata, 
                                                          0, u'S, N')
                    
                    if 'dscFatRisc' in dir(fatRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fatRisco.dscFatRisc', 
                                                          fatRisco.dscFatRisc.cdata, 
                                                          0, u'None')
                    
                    if 'epcEpi' in dir(fatRisco.epcEpi):
                        for epcEpi in fatRisco.epcEpi:
                            
                            if 'utilizEPC' in dir(epcEpi):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'epcEpi.utilizEPC', 
                                                                  epcEpi.utilizEPC.cdata, 
                                                                  1, u'0, 1, 2')
                            
                            if 'eficEpc' in dir(epcEpi):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'epcEpi.eficEpc', 
                                                                  epcEpi.eficEpc.cdata, 
                                                                  0, u'S, N')
                            
                            if 'utilizEPI' in dir(epcEpi):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'epcEpi.utilizEPI', 
                                                                  epcEpi.utilizEPI.cdata, 
                                                                  1, u'0, 1, 2')
                            
                            if 'epc' in dir(epcEpi.epc):
                                for epc in epcEpi.epc:
                                    
                                    if 'codEP' in dir(epc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epc.codEP', 
                                                                          epc.codEP.cdata, 
                                                                          1, u'None')
                                    
                                    if 'dscEpc' in dir(epc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epc.dscEpc', 
                                                                          epc.dscEpc.cdata, 
                                                                          1, u'None')
                                    
                                    if 'eficEpc' in dir(epc):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epc.eficEpc', 
                                                                          epc.eficEpc.cdata, 
                                                                          0, u'S, N')
                            
                            if 'epi' in dir(epcEpi.epi):
                                for epi in epcEpi.epi:
                                    
                                    if 'caEPI' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.caEPI', 
                                                                          epi.caEPI.cdata, 
                                                                          0, u'None')
                                    
                                    if 'dscEPI' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.dscEPI', 
                                                                          epi.dscEPI.cdata, 
                                                                          0, u'None')
                                    
                                    if 'eficEpi' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.eficEpi', 
                                                                          epi.eficEpi.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'medProtecao' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.medProtecao', 
                                                                          epi.medProtecao.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'condFuncto' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.condFuncto', 
                                                                          epi.condFuncto.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'usoInint' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.usoInint', 
                                                                          epi.usoInint.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'przValid' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.przValid', 
                                                                          epi.przValid.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'periodicTroca' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.periodicTroca', 
                                                                          epi.periodicTroca.cdata, 
                                                                          1, u'S, N')
                                    
                                    if 'higienizacao' in dir(epi):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'epi.higienizacao', 
                                                                          epi.higienizacao.cdata, 
                                                                          1, u'S, N')
            
            if 'respReg' in dir(infoExpRisco.respReg):
                for respReg in infoExpRisco.respReg:
                    
                    if 'cpfResp' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.cpfResp', 
                                                          respReg.cpfResp.cdata, 
                                                          1, u'None')
                    
                    if 'nisResp' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.nisResp', 
                                                          respReg.nisResp.cdata, 
                                                          1, u'None')
                    
                    if 'nmResp' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.nmResp', 
                                                          respReg.nmResp.cdata, 
                                                          1, u'None')
                    
                    if 'ideOC' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.ideOC', 
                                                          respReg.ideOC.cdata, 
                                                          1, u'1, 4, 9')
                    
                    if 'dscOC' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.dscOC', 
                                                          respReg.dscOC.cdata, 
                                                          0, u'None')
                    
                    if 'nrOC' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.nrOC', 
                                                          respReg.nrOC.cdata, 
                                                          1, u'None')
                    
                    if 'ufOC' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.ufOC', 
                                                          respReg.ufOC.cdata, 
                                                          1, u'None')
            
            if 'obs' in dir(infoExpRisco.obs):
                for obs in infoExpRisco.obs:
                    
                    if 'metErg' in dir(obs):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'obs.metErg', 
                                                          obs.metErg.cdata, 
                                                          0, u'None')
                    
                    if 'obsCompl' in dir(obs):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'obs.obsCompl', 
                                                          obs.obsCompl.cdata, 
                                                          0, u'None')
                    
                    if 'observacao' in dir(obs):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'obs.observacao', 
                                                          obs.observacao.cdata, 
                                                          0, u'None')
            
            if 'altExpRisco' in dir(infoExpRisco.altExpRisco):
                for altExpRisco in infoExpRisco.altExpRisco:
                    
                    if 'dtAltCondicao' in dir(altExpRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'altExpRisco.dtAltCondicao', 
                                                          altExpRisco.dtAltCondicao.cdata, 
                                                          1, u'None')
                    
                    if 'infoAmb' in dir(altExpRisco.infoAmb):
                        for infoAmb in altExpRisco.infoAmb:
                            
                            if 'codAmb' in dir(infoAmb):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoAmb.codAmb', 
                                                                  infoAmb.codAmb.cdata, 
                                                                  1, u'None')
                            
                            if 'infoAtiv' in dir(infoAmb.infoAtiv):
                                for infoAtiv in infoAmb.infoAtiv:
                                    
                                    if 'dscAtivDes' in dir(infoAtiv):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoAtiv.dscAtivDes', 
                                                                          infoAtiv.dscAtivDes.cdata, 
                                                                          1, u'None')
                            
                            if 'fatRisco' in dir(infoAmb.fatRisco):
                                for fatRisco in infoAmb.fatRisco:
                                    
                                    if 'codFatRis' in dir(fatRisco):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fatRisco.codFatRis', 
                                                                          fatRisco.codFatRis.cdata, 
                                                                          1, u'01.01.01, 01.01.02, 01.01.03, 01.01.04, 01.01.05, 01.01.06, 01.01.07, 01.01.08, 01.01.09, 01.01.10, 01.01.11, 01.01.12, 01.01.13, 01.01.14, 01.01.15, 01.01.16, 01.01.17, 01.01.18, 01.01.19, 01.01.20, 01.01.21, 01.01.22, 01.01.23, 0.101.999, 02.01.01, 02.01.02, 02.01.03, 02.01.04, 02.01.05, 02.01.06, 02.01.07, 02.01.08, 02.01.09, 02.01.10, 02.01.11, 02.01.12, 02.01.13, 02.01.14, 02.01.15, 02.01.16, 02.01.17, 02.01.18, 02.01.19, 02.01.20, 02.01.21, 02.01.22, 02.01.23, 02.01.24, 02.01.25, 02.01.26, 02.01.27, 02.01.28, 02.01.29, 02.01.30, 02.01.31, 02.01.32, 02.01.33, 02.01.34, 02.01.35, 02.01.36, 02.01.37, 02.01.38, 02.01.39, 02.01.40, 02.01.41, 02.01.42, 02.01.43, 02.01.44, 02.01.45, 02.01.46, 02.01.47, 02.01.48, 02.01.49, 02.01.50, 02.01.51, 02.01.52, 02.01.53, 02.01.54, 02.01.55, 02.01.56, 02.01.57, 02.01.59, 02.01.60, 02.01.61, 02.01.62, 02.01.63, 02.01.64, 02.01.65, 02.01.66, 02.01.67, 02.01.68, 02.01.69, 02.01.70, 02.01.71, 02.01.72, 02.01.73, 02.01.74, 02.01.75, 02.01.76, 02.01.77, 02.01.78, 02.01.79, 02.01.80, 02.01.81, 02.01.82, 02.01.83, 02.01.84, 02.01.86, 02.01.87, 02.01.88, 02.01.89, 02.01.90, 02.01.91, 02.01.92, 02.01.93, 02.01.94, 02.01.95, 02.01.96, 02.01.97, 02.01.98, 02.01.99, 0.201.100, 0.201.101, 0.201.102, 0.201.103, 0.201.104, 0.201.105, 0.201.106, 0.201.107, 0.201.108, 0.201.109, 0.201.110, 0.201.111, 0.201.112, 0.201.113, 0.201.114, 0.201.115, 0.201.116, 0.201.117, 0.201.118, 0.201.119, 0.201.121, 0.201.122, 0.201.123, 0.201.124, 0.201.125, 0.201.126, 0.201.127, 0.201.128, 0.201.130, 0.201.131, 0.201.132, 0.201.133, 0.201.135, 0.201.136, 0.201.137, 0.201.138, 0.201.139, 0.201.140, 0.201.141, 0.201.143, 0.201.144, 0.201.145, 0.201.146, 0.201.147, 0.201.148, 0.201.149, 0.201.150, 0.201.151, 0.201.152, 0.201.153, 0.201.154, 0.201.155, 0.201.156, 0.201.157, 0.201.158, 0.201.159, 0.201.160, 0.201.161, 0.201.162, 0.201.163, 0.201.164, 0.201.165, 0.201.166, 0.201.167, 0.201.169, 0.201.170, 0.201.171, 0.201.172, 0.201.173, 0.201.174, 0.201.175, 0.201.176, 0.201.177, 0.201.178, 0.201.179, 0.201.180, 0.201.181, 0.201.182, 0.201.183, 0.201.184, 0.201.185, 0.201.186, 0.201.187, 0.201.188, 0.201.189, 0.201.190, 0.201.191, 0.201.192, 0.201.193, 0.201.194, 0.201.195, 0.201.196, 0.201.197, 0.201.198, 0.201.200, 0.201.201, 0.201.202, 0.201.203, 0.201.204, 0.201.205, 0.201.206, 0.201.207, 0.201.208, 0.201.209, 0.201.210, 0.201.212, 0.201.213, 0.201.214, 0.201.215, 0.201.216, 0.201.217, 0.201.219, 0.201.220, 0.201.223, 0.201.224, 0.201.225, 0.201.226, 0.201.227, 0.201.228, 0.201.229, 0.201.230, 0.201.231, 0.201.232, 0.201.233, 0.201.234, 0.201.235, 0.201.236, 0.201.237, 0.201.238, 0.201.239, 0.201.240, 0.201.241, 0.201.242, 0.201.243, 0.201.244, 0.201.245, 0.201.246, 0.201.247, 0.201.248, 0.201.249, 0.201.250, 0.201.251, 0.201.252, 0.201.253, 0.201.254, 0.201.255, 0.201.257, 0.201.258, 0.201.259, 0.201.260, 0.201.261, 0.201.262, 0.201.263, 0.201.264, 0.201.265, 0.201.266, 0.201.267, 0.201.268, 0.201.269, 0.201.270, 0.201.271, 0.201.272, 0.201.273, 0.201.274, 0.201.275, 0.201.276, 0.201.277, 0.201.278, 0.201.279, 0.201.280, 0.201.281, 0.201.282, 0.201.283, 0.201.284, 0.201.285, 0.201.286, 0.201.287, 0.201.288, 0.201.289, 0.201.290, 0.201.291, 0.201.292, 0.201.293, 0.201.294, 0.201.295, 0.201.296, 0.201.297, 0.201.298, 0.201.299, 0.201.300, 0.201.301, 0.201.302, 0.201.304, 0.201.305, 0.201.306, 0.201.307, 0.201.308, 0.201.309, 0.201.310, 0.201.311, 0.201.312, 0.201.313, 0.201.314, 0.201.315, 0.201.316, 0.201.317, 0.201.318, 0.201.319, 0.201.320, 0.201.321, 0.201.322, 0.201.323, 0.201.324, 0.201.325, 0.201.326, 0.201.327, 0.201.328, 0.201.329, 0.201.330, 0.201.331, 0.201.332, 0.201.333, 0.201.334, 0.201.335, 0.201.336, 0.201.337, 0.201.338, 0.201.339, 0.201.340, 0.201.341, 0.201.342, 0.201.343, 0.201.344, 0.201.345, 0.201.346, 0.201.347, 0.201.348, 0.201.349, 0.201.352, 0.201.353, 0.201.354, 0.201.355, 0.201.356, 0.201.357, 0.201.358, 0.201.359, 0.201.360, 0.201.362, 0.201.363, 0.201.365, 0.201.366, 0.201.367, 0.201.368, 0.201.369, 0.201.370, 0.201.371, 0.201.372, 0.201.373, 0.201.374, 0.201.375, 0.201.376, 0.201.377, 0.201.378, 0.201.380, 0.201.381, 0.201.382, 0.201.383, 0.201.384, 0.201.385, 0.201.386, 0.201.387, 0.201.388, 0.201.389, 0.201.390, 0.201.391, 0.201.392, 0.201.393, 0.201.394, 0.201.395, 0.201.396, 0.201.397, 0.201.398, 0.201.399, 0.201.400, 0.201.401, 0.201.402, 0.201.403, 0.201.404, 0.201.405, 0.201.406, 0.201.407, 0.201.408, 0.201.409, 0.201.410, 0.201.411, 0.201.412, 0.201.413, 0.201.414, 0.201.416, 0.201.417, 0.201.418, 0.201.419, 0.201.420, 0.201.421, 0.201.422, 0.201.423, 0.201.424, 0.201.425, 0.201.426, 0.201.427, 0.201.428, 0.201.429, 0.201.430, 0.201.431, 0.201.432, 0.201.433, 0.201.434, 0.201.435, 0.201.436, 0.201.438, 0.201.440, 0.201.441, 0.201.442, 0.201.445, 0.201.446, 0.201.447, 0.201.448, 0.201.449, 0.201.450, 0.201.451, 0.201.452, 0.201.453, 0.201.455, 0.201.457, 0.201.458, 0.201.459, 0.201.460, 0.201.461, 0.201.462, 0.201.463, 0.201.464, 0.201.465, 0.201.466, 0.201.467, 0.201.468, 0.201.469, 0.201.470, 0.201.471, 0.201.472, 0.201.473, 0.201.474, 0.201.475, 0.201.476, 0.201.477, 0.201.478, 0.201.479, 0.201.480, 0.201.481, 0.201.482, 0.201.483, 0.201.484, 0.201.485, 0.201.486, 0.201.487, 0.201.488, 0.201.489, 0.201.490, 0.201.491, 0.201.492, 0.201.493, 0.201.494, 0.201.495, 0.201.497, 0.201.498, 0.201.499, 0.201.500, 0.201.501, 0.201.502, 0.201.503, 0.201.505, 0.201.506, 0.201.507, 0.201.508, 0.201.509, 0.201.510, 0.201.511, 0.201.512, 0.201.513, 0.201.514, 0.201.515, 0.201.518, 0.201.519, 0.201.520, 0.201.521, 0.201.522, 0.201.523, 0.201.524, 0.201.525, 0.201.526, 0.201.527, 0.201.528, 0.201.529, 0.201.530, 0.201.531, 0.201.532, 0.201.533, 0.201.534, 0.201.535, 0.201.536, 0.201.537, 0.201.539, 0.201.540, 0.201.541, 0.201.542, 0.201.543, 0.201.544, 0.201.545, 0.201.546, 0.201.547, 0.201.548, 0.201.549, 0.201.550, 0.201.552, 0.201.553, 0.201.555, 0.201.556, 0.201.557, 0.201.558, 0.201.559, 0.201.560, 0.201.561, 0.201.562, 0.201.563, 0.201.564, 0.201.565, 0.201.566, 0.201.567, 0.201.568, 0.201.569, 0.201.570, 0.201.571, 0.201.572, 0.201.573, 0.201.574, 0.201.575, 0.201.576, 0.201.577, 0.201.578, 0.201.579, 0.201.580, 0.201.581, 0.201.583, 0.201.584, 0.201.585, 0.201.586, 0.201.587, 0.201.588, 0.201.589, 0.201.590, 0.201.591, 0.201.592, 0.201.593, 0.201.594, 0.201.595, 0.201.596, 0.201.597, 0.201.598, 0.201.599, 0.201.600, 0.201.601, 0.201.602, 0.201.603, 0.201.604, 0.201.605, 0.201.606, 0.201.607, 0.201.608, 0.201.609, 0.201.610, 0.201.611, 0.201.612, 0.201.613, 0.201.614, 0.201.615, 0.201.616, 0.201.617, 0.201.618, 0.201.619, 0.201.620, 0.201.621, 0.201.622, 0.201.623, 0.201.624, 0.201.625, 0.201.626, 0.201.627, 0.201.628, 0.201.629, 0.201.630, 0.201.631, 0.201.632, 0.201.633, 0.201.634, 0.201.635, 0.201.636, 0.201.637, 0.201.638, 0.201.639, 0.201.640, 0.201.641, 0.201.642, 0.201.643, 0.201.644, 0.201.645, 0.201.646, 0.201.648, 0.201.649, 0.201.650, 0.201.651, 0.201.652, 0.201.653, 0.201.654, 0.201.655, 0.201.657, 0.201.658, 0.201.659, 0.201.661, 0.201.662, 0.201.664, 0.201.665, 0.201.666, 0.201.667, 0.201.668, 0.201.670, 0.201.671, 0.201.672, 0.201.673, 0.201.674, 0.201.675, 0.201.676, 0.201.677, 0.201.678, 0.201.679, 0.201.680, 0.201.681, 0.201.682, 0.201.683, 0.201.684, 0.201.685, 0.201.686, 0.201.687, 0.201.688, 0.201.689, 0.201.690, 0.201.691, 0.201.692, 0.201.693, 0.201.694, 0.201.695, 0.201.696, 0.201.697, 0.201.698, 0.201.699, 0.201.700, 0.201.701, 0.201.702, 0.201.703, 0.201.704, 0.201.705, 0.201.706, 0.201.707, 0.201.708, 0.201.709, 0.201.710, 0.201.711, 0.201.712, 0.201.713, 0.201.714, 0.201.715, 0.201.716, 0.201.717, 0.201.718, 0.201.719, 0.201.720, 0.201.721, 0.201.722, 0.201.723, 0.201.724, 0.201.725, 0.201.726, 0.201.727, 0.201.728, 0.201.729, 0.201.730, 0.201.731, 0.201.732, 0.201.733, 0.201.734, 0.201.735, 0.201.736, 0.201.737, 0.201.738, 0.201.739, 0.201.740, 0.201.741, 0.201.742, 0.201.743, 0.201.744, 0.201.745, 0.201.746, 0.201.747, 0.201.748, 0.201.749, 0.201.750, 0.201.751, 0.201.752, 0.201.753, 0.201.754, 0.201.755, 0.201.756, 0.201.758, 0.201.759, 0.201.760, 0.201.761, 0.201.762, 0.201.763, 0.201.764, 0.201.765, 0.201.767, 0.201.768, 0.201.769, 0.201.770, 0.201.771, 0.201.772, 0.201.773, 0.201.774, 0.201.775, 0.201.776, 0.201.777, 0.201.778, 0.201.779, 0.201.780, 0.201.781, 0.201.782, 0.201.783, 0.201.785, 0.201.786, 0.201.787, 0.201.788, 0.201.789, 0.201.999, 03.01.01, 0.301.999, 04.01.01, 04.01.02, 04.01.03, 04.01.04, 04.01.05, 04.01.06, 04.01.07, 04.01.08, 04.01.09, 04.01.10, 04.01.11, 04.01.12, 04.01.13, 04.01.14, 04.01.15, 04.01.16, 04.01.17, 04.01.18, 04.01.19, 04.01.20, 0.401.999, 04.02.01, 04.02.02, 04.02.03, 04.02.04, 04.02.05, 04.02.06, 04.02.07, 04.02.08, 04.02.09, 0.402.999, 04.03.01, 04.03.02, 04.03.03, 04.03.04, 04.03.05, 04.03.06, 04.03.07, 04.03.08, 04.03.09, 04.03.10, 0.403.999, 04.04.01, 04.04.02, 04.04.03, 04.04.04, 04.04.05, 04.04.06, 04.04.07, 04.04.08, 0.404.999, 04.05.01, 04.05.02, 04.05.03, 04.05.04, 04.05.05, 04.05.06, 04.05.07, 04.05.08, 04.05.09, 04.05.10, 04.05.11, 0.405.999, 05.01.01, 05.01.02, 05.01.03, 05.01.04, 05.01.05, 05.01.06, 05.01.07, 05.01.08, 05.01.09, 05.01.10, 05.01.11, 05.01.12, 05.01.13, 05.01.14, 05.01.15, 05.01.16, 05.01.17, 05.01.18, 05.01.19, 05.01.20, 05.01.21, 05.01.22, 05.01.23, 05.01.24, 05.01.25, 05.01.26, 05.01.27, 05.01.28, 05.01.29, 05.01.30, 05.01.31, 05.01.32, 0.501.999, 06.01.01, 07.01.01, 08.01.01, 09.01.01')
                                    
                                    if 'intConc' in dir(fatRisco):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fatRisco.intConc', 
                                                                          fatRisco.intConc.cdata, 
                                                                          0, u'None')
                                    
                                    if 'tecMedicao' in dir(fatRisco):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'fatRisco.tecMedicao', 
                                                                          fatRisco.tecMedicao.cdata, 
                                                                          0, u'None')
                                    
                                    if 'epcEpi' in dir(fatRisco.epcEpi):
                                        for epcEpi in fatRisco.epcEpi:
                                            
                                            if 'utilizEPC' in dir(epcEpi):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'epcEpi.utilizEPC', 
                                                                                  epcEpi.utilizEPC.cdata, 
                                                                                  1, u'0, 1, 2')
                                            
                                            if 'utilizEPI' in dir(epcEpi):
                                                validacoes_lista = validar_campo( validacoes_lista,
                                                                                  'epcEpi.utilizEPI', 
                                                                                  epcEpi.utilizEPI.cdata, 
                                                                                  1, u'0, 1, 2')
                                            
                                            if 'epc' in dir(epcEpi.epc):
                                                for epc in epcEpi.epc:
                                                    
                                                    if 'dscEpc' in dir(epc):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epc.dscEpc', 
                                                                                          epc.dscEpc.cdata, 
                                                                                          1, u'None')
                                                    
                                                    if 'eficEpc' in dir(epc):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epc.eficEpc', 
                                                                                          epc.eficEpc.cdata, 
                                                                                          0, u'S, N')
                                            
                                            if 'epi' in dir(epcEpi.epi):
                                                for epi in epcEpi.epi:
                                                    
                                                    if 'caEPI' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.caEPI', 
                                                                                          epi.caEPI.cdata, 
                                                                                          0, u'None')
                                                    
                                                    if 'eficEpi' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.eficEpi', 
                                                                                          epi.eficEpi.cdata, 
                                                                                          1, u'S, N')
                                                    
                                                    if 'medProtecao' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.medProtecao', 
                                                                                          epi.medProtecao.cdata, 
                                                                                          1, u'S, N')
                                                    
                                                    if 'condFuncto' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.condFuncto', 
                                                                                          epi.condFuncto.cdata, 
                                                                                          1, u'S, N')
                                                    
                                                    if 'przValid' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.przValid', 
                                                                                          epi.przValid.cdata, 
                                                                                          1, u'S, N')
                                                    
                                                    if 'periodicTroca' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.periodicTroca', 
                                                                                          epi.periodicTroca.cdata, 
                                                                                          1, u'S, N')
                                                    
                                                    if 'higienizacao' in dir(epi):
                                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                                          'epi.higienizacao', 
                                                                                          epi.higienizacao.cdata, 
                                                                                          1, u'S, N')
            
            if 'fimExpRisco' in dir(infoExpRisco.fimExpRisco):
                for fimExpRisco in infoExpRisco.fimExpRisco:
                    
                    if 'dtFimCondicao' in dir(fimExpRisco):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'fimExpRisco.dtFimCondicao', 
                                                          fimExpRisco.dtFimCondicao.cdata, 
                                                          1, u'None')
                    
                    if 'infoAmb' in dir(fimExpRisco.infoAmb):
                        for infoAmb in fimExpRisco.infoAmb:
                            
                            if 'codAmb' in dir(infoAmb):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'infoAmb.codAmb', 
                                                                  infoAmb.codAmb.cdata, 
                                                                  1, u'None')
            
            if 'respReg' in dir(infoExpRisco.respReg):
                for respReg in infoExpRisco.respReg:
                    
                    if 'dtIni' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.dtIni', 
                                                          respReg.dtIni.cdata, 
                                                          1, u'None')
                    
                    if 'dtFim' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.dtFim', 
                                                          respReg.dtFim.cdata, 
                                                          0, u'None')
                    
                    if 'nisResp' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.nisResp', 
                                                          respReg.nisResp.cdata, 
                                                          1, u'None')
                    
                    if 'nrOc' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.nrOc', 
                                                          respReg.nrOc.cdata, 
                                                          1, u'None')
                    
                    if 'ufOC' in dir(respReg):
                        validacoes_lista = validar_campo( validacoes_lista,
                                                          'respReg.ufOC', 
                                                          respReg.ufOC.cdata, 
                                                          0, u'None')
    return validacoes_lista