---
layout: default
title: Dupilumab
parent: Evidencia Moderada (L3-L4)
nav_order: 169
evidence_level: L4
indication_count: 10
---

# Dupilumab
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Dupilumab: De Indicación Original No Especificada en el Registro a Bronquitis

## Resumen en Una Frase

Dupilumab es un anticuerpo monoclonal que bloquea el receptor IL-4Rα y se comercializa en Colombia como DUPIXENT®. El texto de los registros sanitarios solo menciona el principio activo, sin indicación original.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, pero la evidencia es indirecta: **1 ensayo clínico** (rinosinusitis crónica) y **6 publicaciones** (sobre todo asma y EPOC) apoyan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice "Dupilumab") |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Dupilumab bloquea la subunidad IL-4Rα. Con ello interrumpe la señalización de IL-4 e IL-13, dos citocinas clave de la inflamación tipo 2. No hay datos detallados del mecanismo de acción en DrugBank, así que esta descripción proviene del análisis de reposicionamiento del propio paquete de evidencia.

El puente biológico plausible son las enfermedades de la vía aérea con inflamación tipo 2, como el asma eosinofílica y la bronquitis plástica eosinofílica. Dupilumab ya cuenta con estudios en asma, EPOC y rinosinusitis crónica. En esos cuadros, bloquear IL-4/IL-13 podría reducir la inflamación de las vías respiratorias.

Aun así, el puntaje de 99.92% es solo una predicción computacional. Ninguno de los estudios aportados evalúa dupilumab en bronquitis general. El único ítem específico de bronquitis es una publicación de baja jerarquía sobre bronquitis plástica eosinofílica pediátrica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Fase 2 | Completado | 33 | Ensayo aleatorizado, doble ciego y controlado con placebo de dupilumab en rinosinusitis crónica sin pólipos nasales. Es un estudio de vía aérea superior, no de bronquitis, y solo apoya de forma indirecta la biología tipo 2. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Metaanálisis de ECA | J Asthma | Evalúa la eficacia y seguridad de dupilumab frente a placebo en asma no controlada, a partir de ensayos aleatorizados. |
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Extensión abierta (TRAVERSE) | Lancet Respir Med | Seguridad y eficacia a largo plazo de dupilumab en asma moderada a grave, más allá de 1 año. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Estudio prospectivo de imagen | Chest | Efecto de la terapia biológica anti-T2 sobre la ventilación pulmonar medida por resonancia magnética en asma dependiente de prednisona. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Revisión | Tuberc Respir Dis | Revisión de terapias farmacológicas para prevenir exacerbaciones de EPOC, incluidos agentes novedosos. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revisión | Expert Opin Pharmacother | Desafíos del manejo del asma asociada a enfermedades de la vía aérea inducidas por el tabaco, entre ellas la bronquitis crónica. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Revisión / basado en casos | Pediatr Pulmonol | Terapias novedosas para la bronquitis plástica eosinofílica pediátrica. Es el único ítem específico de bronquitis y no tiene resumen disponible. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20156864 | DUPIXENT® 200MG (SANOFI-AVENTIS DE COLOMBIA S.A.) | Solución inyectable | No especifica indicación; solo figura el principio activo (Dupilumab) |

Las cinco entradas listadas en los datos corresponden al mismo registro sanitario, por eso se muestra una sola fila. El total reportado es de 20 registros.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay estudios de dupilumab en bronquitis general. La evidencia disponible es indirecta (asma, EPOC, rinosinusitis crónica) y el único ítem específico es una publicación de baja jerarquía sobre bronquitis plástica eosinofílica. El puntaje de TxGNN es una predicción y no confirma eficacia.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que hoy es un vacío bloqueante para el tamizaje de seguridad.
- Consultar el mecanismo de acción detallado en DrugBank.
- Definir el fenotipo de bronquitis a estudiar (por ejemplo, con inflamación tipo 2 o eosinofílica) y buscar estudios específicos de ese fenotipo.
- Confirmar la indicación original aprobada en el registro sanitario, porque el texto actual solo indica el principio activo.
- Revisar los resultados del ensayo NCT04362501 para evaluar su relevancia en vía aérea.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

