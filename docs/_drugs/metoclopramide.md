---
layout: default
title: Metoclopramide
parent: Solo Predicción del Modelo (L5)
nav_order: 438
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Metoclopramide: nueva indicación predicha, Gastroduodenitis (nivel de evidencia L4). Indicación original: No especificada en el registro (el texto aprobado solo indica \"METOCL…"
monitor_inn: "metoclopramide"
predicted_indications: ["gastroduodenitis", "peptic ulcer perforation"]
---

# Metoclopramide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Metoclopramida: De Indicación No Especificada en el Registro a Gastroduodenitis
{: .text-alpha }

## Resumen en Una Frase

La metoclopramida es un fármaco procinético y antiemético con registros sanitarios en Colombia, aunque el texto de indicación del registro solo repite el nombre del fármaco.
El modelo TxGNN predice que podría ser efectivo para **úlcera gástrica**, con **1 ensayo clínico** (de uso procedimental, no terapéutico) y **20 publicaciones**, en su mayoría revisiones antiguas, que respaldan esta dirección de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "METOCLOPRAMIDA") |
| Nueva Indicación Predicha | Úlcera gástrica |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 4) |
| Número de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información de las fuentes consultadas, la metoclopramida es un antagonista del receptor de dopamina D2 y agonista del receptor 5-HT4 que mejora el vaciamiento gástrico y la motilidad antroduodenal. Mecanísticamente, podría ser útil en cuadros ulcerosos acompañados de vaciamiento gástrico retardado o reflujo.

La relación con la nueva indicación es indirecta. La metoclopramida no tiene acción cicatrizante de la úlcera ni antisecretora; de hecho, un estudio doble ciego en voluntarios sanos (PMID 6782467) no halló cambios significativos en la gastrina ni en la secreción ácida. Un estudio preclínico en ratas (PMID 2730234, indexado en otra predicción) sugirió un efecto protector frente a úlceras inducidas, pero no hay confirmación clínica.

El único ensayo registrado usa la metoclopramida como premedicación antes de la endoscopia en hemorragia digestiva alta, es decir, un uso de apoyo al procedimiento y no un tratamiento de la úlcera. La puntuación alta del modelo parece reflejar la cercanía en la red de conocimiento con otras entidades gastrointestinales, más que evidencia biológica o clínica directa.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Fase 4 | Desconocido | 60 | Ensayo aleatorizado doble ciego de metoclopramida como premedicación en hemorragia digestiva alta, para evaluar la necesidad de repetir la endoscopia y la visibilidad de la pared gástrica. No evalúa la cicatrización de la úlcera. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [786607](https://pubmed.ncbi.nlm.nih.gov/786607/) | 1976 | Revisión | Drugs | Revisión de propiedades farmacológicas y uso clínico de la metoclopramida, incluido su papel en la endoscopia de urgencia en hemorragia digestiva alta. |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Revisión | Postgraduate Medicine | Estrategias terapéuticas para úlceras y esofagitis por reflujo que no responden a los tratamientos estándar. |
| [11879596](https://pubmed.ncbi.nlm.nih.gov/11879596/) | 2002 | Revisión | Current Treatment Options in Gastroenterology | Dispepsia funcional (no ulcerosa) y utilidad de evaluar el vaciamiento gástrico. |
| [12825960](https://pubmed.ncbi.nlm.nih.gov/12825960/) | 2003 | Revisión | Drugs | Gastroparesia diabética y opciones de tratamiento limitadas. |
| [8686797](https://pubmed.ncbi.nlm.nih.gov/8686797/) | 1996 | Revisión | American Journal of Surgery | Vaciamiento gástrico retardado tras cirugía gástrica, a menudo por enfermedad ulcerosa péptica. |
| [797497](https://pubmed.ncbi.nlm.nih.gov/797497/) | 1976 | Revisión | Clinical Pharmacokinetics | Fármacos, enfermedades (incluida la úlcera gástrica) y alteración del vaciamiento gástrico. |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | Estudio cruzado aleatorizado doble ciego | MMW Munch Med Wochenschr | Ni domperidona ni metoclopramida modificaron de forma significativa la gastrina ni la secreción ácida en 12 voluntarios sanos. |
| [579607](https://pubmed.ncbi.nlm.nih.gov/579607/) | 1978 | Simposio/revisión | Canadian Journal of Surgery | Tratamiento médico de la úlcera péptica; se menciona el efecto de la metoclopramida sobre el vaciamiento gástrico. |

Nota: la literatura recuperada consiste sobre todo en revisiones antiguas sobre motilidad gástrica, gastroparesia y reflujo; no hay ensayos clínicos que demuestren la cicatrización de úlceras con metoclopramida.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19955371 | METOCLOPRAMIDA 10 MG TABLETAS | Tableta | METOCLOPRAMIDA (vigente) |
| 19956364 | ENZIMAR GOTAS PEDIATRICAS | Solución oral | METOCLOPRAMIDA (vigente) |
| 19941418 | METOCLOPRAMIDA10 MG | Tableta | METOCLOPRAMIDA (vigente) |
| 19927476 | PLASIL® INYECTABLE | Solución inyectable | METOCLOPRAMIDA (vigente) |

Los cuatro registros están cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** hipertensión, epilepsia, trastornos de ansiedad, porfiria, cirrosis hepática, insuficiencia renal, feocromocitoma, úlcera péptica activa, síndrome neuroléptico maligno, discinesia tardía, enfermedad de Parkinson y otros trastornos parkinsonianos, distonía de torsión, entre otras.
- **Interacciones farmacológicas:** se identificaron 670 interacciones potenciales. Entre las de nivel **mayor** figuran **tramadol** y **amisulprida**. Hay numerosas interacciones de nivel moderado, por ejemplo con opioides (fentanilo, codeína, dihidrocodeína, alfentanilo), benzodiacepinas (alprazolam), antihistamínicos (clorfeniramina, cetirizina), amitriptilina, amantadina, etanol y abiraterona.

Nota importante: la contraindicación por úlcera péptica activa figura en el grafo de conocimiento, lo que debe aclararse antes de considerar cualquier uso en enfermedad ulcerosa. Además, los procinéticos generalmente no se recomiendan ante sospecha de obstrucción mecánica o perforación.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita al nivel L4: un único ensayo de uso procedimental y literatura mayormente indirecta, sin demostración de efecto cicatrizante ni antisecretor. A esto se suman la ausencia de registros vigentes en Colombia y una señal de contraindicación en úlcera péptica activa.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto (advertencias y contraindicaciones oficiales), ya que esta información falta y bloquea el análisis de seguridad.
- Obtener datos del mecanismo de acción desde fuentes farmacológicas de referencia.
- Aclarar la indicación original aprobada, pues el registro solo repite el nombre del fármaco.
- Valorar si el posible beneficio se limita a síntomas (náuseas, vaciamiento retardado) o a uso procedimental, en lugar de tratamiento de la úlcera.
- Generar estudios clínicos específicos que evalúen la cicatrización de la úlcera, y resolver la contradicción con la contraindicación en úlcera péptica activa.
- Confirmar la situación regulatoria: los registros están cancelados, por lo que cualquier uso requeriría un nuevo trámite ante INVIMA.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

