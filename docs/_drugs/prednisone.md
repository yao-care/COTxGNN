---
layout: default
title: Prednisone
parent: Evidencia Alta (L1-L2)
nav_order: 332
evidence_level: L2
indication_count: 10
---

# Prednisone
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Prednisona: De Afecciones Inflamatorias a Alopecia Areata

## Resumen en Una Frase

La prednisona es un corticosteroide sistémico de uso oral, indicado en una amplia variedad de afecciones inflamatorias.
El modelo TxGNN predice que podría ser efectiva para **alopecia areata**.
Hay **35 ensayos clínicos** y **20 publicaciones** asociados. Solo **1 ensayo de Fase 3** evalúa prednisona en esta enfermedad, y lo hace como complemento del metotrexato, no como comparación independiente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo cita "PREDNISONA" como texto de indicación, sin detallar usos. La farmacología la describe como tratamiento de "afecciones inflamatorias diversas". |
| Nueva Indicación Predicha | Alopecia areata |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 7 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información farmacológica disponible, la prednisona actúa sobre el receptor de glucocorticoides (gen *NR3C1*) y se usa en múltiples enfermedades inflamatorias. Su eficacia antiinflamatoria e inmunosupresora está bien establecida.

La alopecia areata es un ataque autoinmune mediado por linfocitos T contra el folículo piloso. Los glucocorticoides sistémicos suprimen esa inflamación, por lo que el vínculo mecanístico es plausible y clínicamente reconocido. Sus límites conocidos son la recaída al suspender el tratamiento y la toxicidad acumulada por el uso prolongado.

El puntaje de TxGNN (0.9999) es coherente con la literatura, pero no aporta evidencia independiente. Conviene leerlo como una señal de consistencia con el conocimiento existente, no como una prueba de eficacia.

---

## Evidencia de Ensayos Clínicos

Se registraron 35 ensayos asociados a esta predicción. La mayoría son estudios de lupus eritematoso sistémico o cutáneo con otros fármacos. Solo NCT02037191 evalúa prednisona directamente en alopecia areata. Los demás se incluyen como contexto y no respaldan la prednisona en esta enfermedad.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02037191](https://clinicaltrials.gov/study/NCT02037191) | Fase 3 | Completado | 90 | ECA doble ciego en alopecia areata grave: metotrexato vs placebo, con tratamiento secundario de metotrexato + prednisona en dosis baja. Probablemente corresponde al estudio PMID 36884234, aunque ese vínculo se infiere por el título y no está confirmado. La prednisona es un componente añadido. |
| [NCT03616964](https://clinicaltrials.gov/study/NCT03616964) | Fase 3 | Completado | 778 | Baricitinib vs placebo. El título indica lupus eritematoso sistémico, aunque el análisis automático lo asoció a alopecia areata. No evalúa prednisona. |
| [NCT03843125](https://clinicaltrials.gov/study/NCT03843125) | Fase 3 | Terminado anticipadamente | 1147 | Extensión de seguridad a largo plazo de baricitinib (lupus). No evalúa prednisona. |
| [NCT05162586](https://clinicaltrials.gov/study/NCT05162586) | Fase 2 | Completado | 456 | Enpatoran vs placebo en lupus sistémico y cutáneo. Es otro agente. |
| [NCT07332481](https://clinicaltrials.gov/study/NCT07332481) | Fase 3 | Reclutando | 202 | ELOWEN-1: enpatoran vs placebo en manifestaciones cutáneas de lupus. No está dirigido a prednisona. |
| [NCT07515014](https://clinicaltrials.gov/study/NCT07515014) | Fase 2 | Reclutando | 256 | E6742 vs placebo en lupus, con corticosteroide oral de fondo (prednisona o equivalente). No está dirigido a prednisona. |
| [NCT07840287](https://clinicaltrials.gov/study/NCT07840287) | Fase 3 | Aún no recluta | 404 | Extensión abierta de enpatoran en lupus cutáneo. Sin evidencia sobre prednisona. |
| [NCT01511536](https://clinicaltrials.gov/study/NCT01511536) | Fase 1/2 | Completado | 38 | Cabazitaxel + abiraterona + prednisona en cáncer de próstata. La prednisona es fármaco de fondo en una enfermedad no relacionada. |
| [NCT01972217](https://clinicaltrials.gov/study/NCT01972217) | Fase 2 | Completado | 158 | Olaparib + abiraterona en cáncer de próstata. Coincidencia probablemente por nombre del fármaco. |
| [NCT01652261](https://clinicaltrials.gov/study/NCT01652261) | Fase 3 | Retirado | 0 | Linfoma de Hodgkin. Sin relación con alopecia areata. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | ECA | JAMA Dermatology | ECA doble ciego de 2 pasos: metotrexato solo vs metotrexato + prednisona en dosis baja en alopecia areata totalis/universalis. El resumen disponible no incluye resultados. |
| [1444509](https://pubmed.ncbi.nlm.nih.gov/1444509/) | 1992 | Revisión | Archives of Dermatology | Revisión de terapias para alopecia areata grave. Algunos fármacos son eficaces en algún grado, pero los estudios son tan heterogéneos que no permiten comparaciones útiles. |
| [37467740](https://pubmed.ncbi.nlm.nih.gov/37467740/) | 2023 | Serie de casos (8) | Clin Exp Dermatol | Baricitinib con corticosteroides en dosis bajas en alopecia areata muy grave, donde baricitinib solo funciona poco. Los autores reportan una mejoría mayor. |
| [41958306](https://pubmed.ncbi.nlm.nih.gov/41958306/) | 2026 | Serie de casos retrospectiva | JEADV | Baricitinib más prednisona en dosis baja en alopecia areata muy grave. No hay resumen disponible. |
| [791152](https://pubmed.ncbi.nlm.nih.gov/791152/) | 1976 | Seguimiento de cohorte | Archives of Dermatology | 18 pacientes tratados con prednisona en días alternos. Hubo respuesta inicial, pero el beneficio a largo plazo no fue sustancial. Reportó efectos adversos (acné, obesidad, opacidades del cristalino, hipertensión leve). |
| [20804894](https://pubmed.ncbi.nlm.nih.gov/20804894/) | 2010 | Cohorte observacional | Ann Dermatol Venereol | Prednisona oral en pulso mensual para alopecia areata. El resumen disponible solo describe el objetivo. |
| [26735937](https://pubmed.ncbi.nlm.nih.gov/26735937/) | 2016 | Estudio clínico | Dermatology | Metotrexato con corticosteroides en dosis baja a moderada en alopecia areata grave. El resumen disponible solo cita el contexto. |
| [9732014](https://pubmed.ncbi.nlm.nih.gov/9732014/) | 1998 | Estudio clínico | Int J Dermatol | Corticosteroides sistémicos en alopecia areata grave. El resumen los presenta como un tratamiento eficaz. |
| [8996277](https://pubmed.ncbi.nlm.nih.gov/8996277/) | 1997 | Estudio clínico | J Am Acad Dermatol | Ciclosporina sistémica con prednisona en dosis baja en alopecia areata crónica grave, con evaluación clínica e inmunopatológica. No hay resumen disponible. |
| [23962142](https://pubmed.ncbi.nlm.nih.gov/23962142/) | 2013 | Reporte de caso | J Cutan Pathol | Mucinosis folicular con alopecia difusa similar a alopecia areata. Se resolvió por completo con prednisona oral. |

---

## Información de Mercado en Colombia

El paquete de evidencia lista 5 entradas con el mismo número de registro. Aquí se presenta una sola vez, porque las entradas son idénticas. El total declarado es de 7 registros sanitarios.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19906237 | PREDNISONA MK 50 MG TABLETAS (Tecnoquímicas S.A.) | Tableta (vía oral) | "PREDNISONA" (el registro no detalla indicaciones) |

---

## Consideraciones de Seguridad

- **Señales de la literatura**: el seguimiento de prednisona en días alternos en alopecia areata (PMID 791152) reportó acné, obesidad, opacidades del cristalino e hipertensión leve. El beneficio a largo plazo no fue sustancial.
- **Limitaciones del uso prolongado**: hay recaída tras la suspensión y toxicidad acumulada por esteroides.

Para advertencias, contraindicaciones e interacciones farmacológicas, consultar el prospecto. No hay datos de interacción entre fármacos en el paquete de evidencia.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
- Hay un ECA de Fase 3 completado en alopecia areata que incluye prednisona en dosis baja, respaldado por un ECA publicado y por series de casos. Sin embargo, la prednisona actúa como complemento del metotrexato y no como comparador independiente, y la evidencia directa es limitada.
- La recaída tras suspender y la toxicidad acumulada exigen límites de dosis y duración.

**Para avanzar se necesita:**
- Confirmar que NCT02037191 corresponde a la publicación PMID 36884234 y revisar sus resultados completos.
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) y los datos de mecanismo de acción de DrugBank.
- Definir esquema de dosis y duración, con plan de monitoreo de efectos adversos de esteroides y de recaída.
- Aclarar la indicación real del registro sanitario, que solo cita el nombre del principio activo.
- Comparar con las alternativas actuales, como los inhibidores de JAK.

Las otras indicaciones predichas (rango 2 a 10) tienen evidencia más débil y quedan en Hold. La única excepción es tenosinovitis, marcada como pregunta de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

