---
layout: default
title: Ertapenem
parent: Evidencia Moderada (L3-L4)
nav_order: 183
evidence_level: L4
indication_count: 2
---

# Ertapenem
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Ertapenem: De Antibacteriano Carbapenémico a Artritis Bacteriana

## Resumen en Una Frase

Ertapenem es un antibiótico carbapenémico comercializado en Colombia. El registro sanitario no detalla su indicación aprobada, solo repite el nombre del fármaco.
El modelo TxGNN predice que podría ser efectivo para **artritis bacteriana**, pero hoy hay **0 ensayos clínicos** y solo reportes de casos, cohortes y estudios in vitro de apoyo indirecto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto registrado solo dice «ERTAPENEM») |
| Nueva Indicación Predicha | Artritis bacteriana |
| Puntaje de Predicción TxGNN | 99.72% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, ertapenem es un carbapenémico, una clase de antibióticos betalactámicos de amplio espectro. Mecanísticamente podría ser aplicable a la artritis bacteriana.

En general, los carbapenémicos se unen a las proteínas fijadoras de penicilina (PBP) e inhiben la síntesis de la pared celular bacteriana. Este es conocimiento de la clase farmacológica y no un dato del paquete de evidencia. Ertapenem tiene actividad contra enterobacterias y anaerobios, que son patógenos frecuentes en infecciones de hueso y articulación, sobre todo cuando son resistentes a cefalosporinas de tercera generación.

La artritis bacteriana (séptica) es una infección causada por bacterias, así que la predicción es una extensión dentro del espectro antibacteriano ya conocido y no un mecanismo nuevo. El puntaje del modelo es alto, pero no hay ensayos clínicos que lo respalden, y la relación con la indicación original no se pudo verificar por falta de datos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Cohorte retrospectiva | Antimicrob Agents Chemother | 306 pacientes con ertapenem ambulatorio prolongado. Las indicaciones más comunes fueron infecciones intraabdominales (38%) y neumonía (12%), y también hubo infecciones de hueso y articulación. |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Reporte de caso | J Chemother | Artritis séptica de muñeca por *Klebsiella pneumoniae* tratada con éxito con ertapenem y levofloxacino (sin resumen disponible). |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Reporte de caso | BMJ Case Reports | Osteomielitis por *Citrobacter koseri* en pie diabético con gota aguda concomitante, tratada con éxito con ertapenem. |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | Preclínico (in vitro) | Diagn Microbiol Infect Dis | Auranofina restauró la sensibilidad de *E. coli* resistente a carbapenémicos frente a ertapenem. Sin relación directa con artritis. |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Reporte de caso + revisión | Anaerobe | Primer caso de artritis séptica y osteomielitis de hombro por *Clostridium paraputrificum*. No es específico de ertapenem. |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Reporte de caso + revisión | J Investig Med High Impact Case Rep | Artritis séptica por *Prevotella bivia* en adulta inmunocompetente. No es específico de ertapenem. |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Cohorte | J Antimicrob Chemother | 10 pacientes con betalactámico subcutáneo como terapia supresora en infecciones de hueso y articulación. No es específico de ertapenem. |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Observacional | Clin Lab | Distribución de patógenos y resistencia en infecciones óseas y articulares en menores de 4 años. |
| [41878879](https://pubmed.ncbi.nlm.nih.gov/41878879/) | 2026 | Observacional | J Antimicrob Chemother | Temocilina como alternativa a carbapenémicos en infecciones óseas y articulares por enterobacterias resistentes. No evalúa ertapenem. |
| [29183082](https://pubmed.ncbi.nlm.nih.gov/29183082/) | 2017 | Revisión | JAMA | Avances en hidradenitis supurativa. Poca relevancia para la indicación predicha. |

La evidencia es débil. Solo dos publicaciones (casos de artritis séptica y osteomielitis) muestran uso de ertapenem en infecciones articulares u óseas, y ninguna es un ensayo controlado.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20117466 | ERTAGRAM® 1 G (EUGIA PHARMA SPECIALITIES LIMITED) | Polvo liofilizado para reconstituir a solución inyectable | No detallada en el registro (solo figura «ERTAPENEM») |

El paquete indica 10 registros en total. Los cinco que llegaron con detalle corresponden al mismo número de registro, por eso se muestran una sola vez. También figura una forma de polvo estéril para reconstituir a solución inyectable.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es alto (99.72%), pero no hay ensayos clínicos para artritis bacteriana y la literatura se limita a reportes de casos y estudios observacionales, en su mayoría indirectos (nivel L4). Además, faltan los datos de seguridad y del mecanismo de acción, por lo que no se puede avanzar a una evaluación de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante.
- Obtener el mecanismo de acción desde DrugBank para verificar el vínculo mecanístico.
- Aclarar la indicación aprobada en el registro sanitario, ya que solo figura el nombre del fármaco.
- Buscar o diseñar estudios comparativos de ertapenem en artritis séptica e infecciones de hueso y articulación.
- Confirmar la compatibilidad de vía de administración, hoy pendiente.

**Nota adicional:** la segunda predicción del modelo, infección por *Staphylococcus aureus*, tiene un ensayo de Fase 2 en curso ([NCT04886284](https://clinicaltrials.gov/study/NCT04886284), cefazolina más ertapenem en bacteriemia por SASM, 60 participantes, reclutando). También cuenta con series de casos y cohortes (nivel L3). Podría ser una línea más sólida para priorizar.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

