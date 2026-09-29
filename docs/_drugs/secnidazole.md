---
layout: default
title: Secnidazole
parent: Solo Predicción del Modelo (L5)
nav_order: 356
evidence_level: L5
indication_count: 7
---

# Secnidazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Secnidazol: De Vaginosis Bacteriana y Tricomoniasis a Vaginitis Atrófica Posmenopáusica

## Resumen en Una Frase

Secnidazol es un antimicrobiano del grupo de los 5-nitroimidazoles, comercializado en Colombia. El texto del registro sanitario no detalla la indicación, pero la literatura lo asocia con vaginosis bacteriana y tricomoniasis. El modelo TxGNN predice que podría ser efectivo para **vaginitis atrófica posmenopáusica** (puntaje 99.70%), pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice "Secnidazol"). Según la literatura: vaginosis bacteriana y tricomoniasis |
| Nueva Indicación Predicha | Vaginitis atrófica posmenopáusica |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Por la información conocida, secnidazol es un 5-nitroimidazol. Su forma reducida daña el ADN de anaerobios y protozoarios sensibles, y por eso es eficaz en infecciones vaginales como la vaginosis bacteriana y la tricomoniasis.

**En este caso la predicción principal es poco plausible.** La vaginitis atrófica se debe a la deficiencia de estrógenos, no a un patógeno anaerobio o protozoario sensible a nitroimidazoles. Los datos no sustentan ningún mecanismo para secnidazol en esta enfermedad. El puntaje alto probablemente refleja cercanía en el grafo de conocimiento con otras entidades de vaginitis, no una relación biológica real.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para vaginitis atrófica posmenopáusica.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para vaginitis atrófica posmenopáusica.

---

## Otras Indicaciones Predichas con Evidencia

Entre las 7 indicaciones predichas, solo tres tienen ensayos o publicaciones. Ninguna es un reposicionamiento novedoso.

| Indicación | Puntaje TxGNN | Nivel | Decisión | Comentario |
|------|------|------|------|------|
| Flujo vaginal | 99.41% | L1 | Proceed with Guardrails | Es un síntoma de vaginosis bacteriana y tricomoniasis, es decir, usos ya establecidos |
| Vulvovaginitis tricomonal | 99.37% | L1 | Proceed with Guardrails | Uso establecido. Ningún ensayo figura directamente bajo esta indicación |
| Candidiasis vulvovaginal | 99.16% | L4 | Research Question | Secnidazol no tiene actividad antifúngica establecida |

Las otras cuatro predicciones (vaginitis atrófica, úlcera vulvar, neoplasia vulvar y leucoplasia vaginal) son solo predicciones del modelo (L5, Hold), sin ensayos ni literatura.

**Ensayos clínicos (flujo vaginal):**

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03935217](https://clinicaltrials.gov/study/NCT03935217) | Fase 3 | Completado | 147 | Dosis oral única de Solosec® 2 g vs placebo (tratamiento diferido, doble ciego) en tricomoniasis. El título está truncado y se infiere que es el ensayo pivotal (no confirmado) |
| [NCT02147899](https://clinicaltrials.gov/study/NCT02147899) | Fase 2 | Completado | 215 | SYM-1219 (secnidazol) vs placebo, aleatorizado y doble ciego, en vaginosis bacteriana |
| [NCT02111629](https://clinicaltrials.gov/study/NCT02111629) | Fase 3 | Completado | 118 | Fluconazol + secnidazol en flujo vaginal sintomático (Bogotá, Colombia). La combinación impide atribuir el efecto a secnidazol solo |
| [NCT03937869](https://clinicaltrials.gov/study/NCT03937869) | Fase 4 | Completado | 40 | Estudio abierto de seguridad de dosis única de 2 g en adolescentes con vaginosis bacteriana. No aporta eficacia comparativa |
| [NCT05033743](https://clinicaltrials.gov/study/NCT05033743) | Fase 2/3 | Completado | 24 | Secnidazol semanal durante 18 semanas para prevenir vaginosis bacteriana recurrente. Piloto pequeño y uso distinto |

**Literatura destacada:**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28867602](https://pubmed.ncbi.nlm.nih.gov/28867602/) | 2017 | ECA | Am J Obstet Gynecol | Fase 3 doble ciego controlado con placebo de secnidazol 2 g en dosis única para vaginosis bacteriana |
| [20885970](https://pubmed.ncbi.nlm.nih.gov/20885970/) | 2010 | ECA | Infect Dis Obstet Gynecol | Fase 3 de no inferioridad, secnidazol vs metronidazol en vaginosis bacteriana |
| [33768237](https://pubmed.ncbi.nlm.nih.gov/33768237/) | 2021 | ECA (probable Fase 3; por confirmar) | Clin Infect Dis | Eficacia y seguridad de secnidazol en dosis única vs placebo en tricomoniasis |
| [31129560](https://pubmed.ncbi.nlm.nih.gov/31129560/) | 2019 | Revisión sistemática y metaanálisis | Eur J Obstet Gynecol Reprod Biol | Eficacia y seguridad de secnidazol 2 g en dosis única para vaginosis bacteriana |
| [39463760](https://pubmed.ncbi.nlm.nih.gov/39463760/) | 2024 | Revisión sistemática y metaanálisis en red | Front Cell Infect Microbiol | Comparación de eficacia y seguridad de distintos fármacos en vaginosis bacteriana |
| [29323627](https://pubmed.ncbi.nlm.nih.gov/29323627/) | 2018 | Estudio abierto Fase 3 | J Womens Health | Seguridad de dosis única de 2 g en mujeres y adolescentes con vaginosis bacteriana |

---

## Información de Mercado en Colombia

Hay 20 registros en total. Los datos recibidos solo incluyen dos registros distintos (el 43991 aparece repetido y se muestra una sola vez).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20085584 | Secnidazol 1 g tabletas (Pentacoop S.A.) | Tableta recubierta | Solo figura "Secnidazol" (sin indicación detallada) |
| 43991 | Secnidazol 500 mg tabletas (Colmed Ltda) | Tableta | Solo figura "Secnidazol" (sin indicación detallada) |

También hay formas orales en tableta cubierta con película.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (vaginitis atrófica posmenopáusica) es solo del modelo, sin estudios y sin mecanismo plausible, ya que la enfermedad es hormonal y no infecciosa. Las indicaciones con evidencia sólida (vaginosis bacteriana y tricomoniasis) son usos ya establecidos, no reposicionamiento.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para verificar indicaciones, advertencias y contraindicaciones autorizadas
- Completar los datos del mecanismo de acción (DrugBank)
- Confirmar la fase y el diseño de la publicación PMID 33768237 y su vínculo con NCT03935217
- Para el flujo vaginal y la tricomoniasis: limitar el uso a casos confirmados por NAAT, microscopía o criterios clínicos, tratar a las parejas y hacer seguimiento
- No priorizar vaginitis atrófica, úlcera vulvar, neoplasia vulvar ni leucoplasia vaginal sin evidencia mecanística nueva

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

