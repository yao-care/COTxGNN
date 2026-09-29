---
layout: default
title: Ciprofloxacin
parent: Evidencia Moderada (L3-L4)
nav_order: 127
evidence_level: L3
indication_count: 10
---

# Ciprofloxacin
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

# Ciprofloxacino: De Antibacteriano (indicación no detallada en el registro) a Esclerodermia Difusa

## Resumen en Una Frase

Ciprofloxacino es un antibiótico de la familia de las fluoroquinolonas. En Colombia está registrado en solución inyectable, pero el registro sanitario no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa**, con **0 ensayos clínicos** registrados y **2 publicaciones** que actualmente respaldan esta dirección. Una de ellas es un estudio clínico pequeño cuyo diseño y resultados no se pudieron verificar.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto registrado solo dice "CIPROFLOXACINA") |
| Nueva Indicación Predicha | Esclerodermia difusa |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de este medicamento en la información recibida. Según lo conocido, ciprofloxacino es una fluoroquinolona antibacteriana. Su eficacia contra infecciones bacterianas está establecida, pero el registro colombiano no detalla la indicación. Mecanísticamente, la predicción hacia esclerodermia difusa podría explicarse por dos vías.

1. **Efecto antifibrótico en la piel.** Lo sugiere el título de un estudio de 2010 (PMID 20507401). Este mecanismo no está establecido con los datos disponibles. Del estudio solo se obtuvo el título y un resumen truncado, por lo que su diseño y resultados no se pudieron verificar.
2. **Tratamiento del sobrecrecimiento bacteriano del intestino delgado.** Esta complicación es frecuente en la esclerosis sistémica y provoca diarrea crónica y pérdida de peso. Aquí el antibiótico actuaría sobre una complicación de la enfermedad, no sobre la enfermedad de base.

La relación con la indicación original es indirecta. Es plausible que un antibiótico ayude en las complicaciones infecciosas o digestivas. Que modifique la fibrosis cutánea sigue siendo una hipótesis.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Estudio clínico pequeño (descrito como ensayo aleatorizado, doble ciego y controlado; diseño sin verificar) | The Journal of Dermatology | Evalúa si el ciprofloxacino oral reduce la gravedad de la esclerodermia, con la fibrosis de la piel como objetivo. El resumen disponible está truncado y no permite conocer los resultados. |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Estudio observacional/diagnóstico | British Journal of Rheumatology | Estudia a 24 pacientes con esclerosis sistémica y síntomas de malabsorción, 6 de ellos con la forma difusa. Detecta sobrecrecimiento bacteriano del intestino delgado y describe el resultado del tratamiento. Es evidencia indirecta. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20026284 | CIPROFLOXACINA 100 MG/10 ML SOLUCION INYECTABLE (Laboratorios Ryan de Colombia S.A.S.) | Solución inyectable | CIPROFLOXACINA (sin indicación detallada) |

El sistema reporta 20 registros en total. Las entradas recibidas para este informe corresponden todas al mismo registro sanitario, por lo que se muestra una sola vez.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos registrados para esclerodermia difusa. La única señal clínica directa es un estudio pequeño cuyo diseño y resultados no se pudieron verificar. La alta puntuación del modelo (99.87%) no compensa esa falta de evidencia. Además, no hay información de seguridad disponible, así que la hipótesis se mantiene como pregunta de investigación.

**Para avanzar se necesita:**
- Obtener el texto completo del estudio PMID 20507401 y verificar su diseño, tamaño de muestra y resultados.
- Buscar y registrar ensayos clínicos en esclerodermia (ClinicalTrials.gov, ICTRP).
- Descargar y analizar el prospecto de INVIMA para completar las advertencias y contraindicaciones, y confirmar la indicación aprobada.
- Obtener el mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Evaluar la tolerabilidad del uso prolongado del antibiótico en pacientes con esclerodermia.

**Nota adicional:** en el mismo paquete de evidencia, la predicción de **peste septicémica** (posición 10) tiene evidencia L1, con ensayos aleatorizados de ciprofloxacino en peste bubónica. Conviene evaluarla por separado, porque su respaldo es mucho más sólido que el de la esclerodermia difusa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

