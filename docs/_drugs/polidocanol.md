---
layout: default
title: Polidocanol
parent: Solo Predicción del Modelo (L5)
nav_order: 522
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Polidocanol: nueva indicación predicha, Várices esofágicas con sangrado (nivel de evidencia L5). Indicación original: Polidocanol"
monitor_inn: "POLIDOCANOL"
predicted_indications: ["esophageal varices with bleeding", "esophageal varices without bleeding", "Immunoerythromyeloid hypoplasia", "pigmented paravenous retinochoroidal atrophy", "progressive bifocal chorioretinal atrophy", "X-linked retinal dysplasia", "monosomy X", "cone dystrophy", "oligocone trichromacy", "retinoschisis of fovea"]
---

# Polidocanol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Polidocanol: De Indicación No Especificada a Várices Esofágicas con Sangrado

## Resumen en Una Frase

Polidocanol es un agente esclerosante que cuenta con registros sanitarios en Colombia (actualmente cancelados), pero cuyo texto de indicación aprobada no detalla un uso clínico específico.
El modelo TxGNN predice que podría ser efectivo para **várices esofágicas con sangrado**,
con **0 ensayos clínicos registrados** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Polidocanol (el registro sanitario no detalla una indicación específica) |
| Nueva Indicación Predicha | Várices esofágicas con sangrado |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L1 (según la clasificación de los datos compilados; ver nota en la sección de literatura) |
| Estado de Mercado en Colombia | Solo cancelados |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento establecido en la literatura, polidocanol es un esclerosante de tipo detergente que daña el endotelio vascular, provocando trombosis y fibrosis del vaso en el que se inyecta.

La escleroterapia endoscópica de várices esofágicas aplica directamente este mecanismo para obliterar las várices que sangran. Por ello, la predicción del modelo es mecanísticamente coherente. Cabe señalar que no se trata de una señal novedosa de reposicionamiento: es un uso clínico ya establecido (incluido el uso fuera de indicación en algunas regiones) y descrito en publicaciones desde la década de 1980.

Dado que el mercado colombiano muestra únicamente registros cancelados, debe verificarse la disponibilidad real del producto antes de cualquier plan de uso.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se priorizan los estudios aleatorizados, seguidos de revisiones y otros diseños.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9255525](https://pubmed.ncbi.nlm.nih.gov/9255525/) | 1997 | ECA | Endoscopy | Estudio prospectivo de cianoacrilato con polidocanol, o polidocanol solo, en el manejo de urgencia y a largo plazo de várices esofágicas en cirróticos |
| [10385713](https://pubmed.ncbi.nlm.nih.gov/10385713/) | 1999 | ECA | Gastrointest Endosc | Ligadura frente a ligadura combinada con escleroterapia en várices esofágicas con sangrado |
| [2693076](https://pubmed.ncbi.nlm.nih.gov/2693076/) | 1989 | ECA | Endoscopy | Etanolamina vs. polidocanol en erradicación de várices (81% vs. 64%, sin diferencia significativa) |
| [29473522](https://pubmed.ncbi.nlm.nih.gov/29473522/) | 2017 | Revisión | Curr Clin Pharmacol | Revisión basada en evidencia de usos fuera de indicación de polidocanol |
| [32517718](https://pubmed.ncbi.nlm.nih.gov/32517718/) | 2020 | Revisión sistemática | BMC Gastroenterol | Riesgo de resangrado de várices gastroesofágicas tras tratamiento inicial con cianoacrilato |
| [7942715](https://pubmed.ncbi.nlm.nih.gov/7942715/) | 1994 | Metaanálisis | Am J Gastroenterol | Escleroterapia endoscópica profiláctica y su efecto sobre la supervivencia |
| [36509625](https://pubmed.ncbi.nlm.nih.gov/36509625/) | 2023 | Cohorte | Arch Pediatr | Escleroterapia con polidocanol para várices cardiales en niños y adolescentes |
| [10434360](https://pubmed.ncbi.nlm.nih.gov/10434360/) | 1999 | Comparativo | J UOEH | Ligadura endoscópica vs. escleroterapia con polidocanol: hemostasia 100% en ambos; resangrado 40.0% vs. 29.6% |
| [6609102](https://pubmed.ncbi.nlm.nih.gov/6609102/) | 1984 | Cohorte (eventos adversos) | Gut | Estenosis o disfagia en 59% de 34 pacientes tras escleroterapia con polidocanol al 3% |
| [20737152](https://pubmed.ncbi.nlm.nih.gov/20737152/) | 2011 | Serie de casos | Eur Radiol | Escleroterapia con espuma de polidocanol en BRTO para várices gástricas fúndicas |

**Nota:** los tres ECA citados son de tamaño modesto y antiguos, y evalúan en su mayoría el esclerosante dentro de estrategias endoscópicas; la guía actual favorece la ligadura con bandas. Por ello el nivel L1 debe interpretarse con cautela.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20018886 | ETOXIVEN® 3% | Solución inyectable | Polidocanol (estado: cancelado) |
| 20017789 | ETOXIVEN® 1% | Solución inyectable | Polidocanol (estado: cancelado) |

---

## Consideraciones de Seguridad

- **Eventos adversos descritos en la literatura:** tras escleroterapia endoscópica con polidocanol al 3% se observaron estenosis esofágica o disfagia en 59% de los pacientes de una cohorte (20 de 34). Se describe además riesgo de ulceración, y la escleroterapia puede agravar la hipertensión portal al suprimir cortocircuitos portosistémicos.

No se dispone de datos de interacciones farmacológicas en la información compilada. Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La escleroterapia con polidocanol para várices esofágicas con sangrado tiene respaldo en varios estudios aleatorizados y cohortes, y es un uso clínico ya establecido. Sin embargo, los registros colombianos están cancelados, no hay ensayos clínicos registrados y la práctica actual prefiere la ligadura con bandas, por lo que se requieren salvaguardas.

**Para avanzar se necesita:**
- Verificar la disponibilidad comercial y el estado regulatorio vigente del producto en Colombia (ambos registros están cancelados)
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones)
- Confirmar el mecanismo de acción en DrugBank
- Definir un plan de monitoreo de eventos adversos (estenosis, ulceración, resangrado) y comparar frente a la ligadura con bandas
- Otras indicaciones predichas (por ejemplo, várices sin sangrado) presentan evidencia indirecta (L3) y se consideran preguntas de investigación; las predichas de rango inferior (enfermedades retinianas, monosomía X, entre otras) carecen de evidencia y de plausibilidad mecanística, por lo que se recomienda mantenerlas en espera (Hold)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

