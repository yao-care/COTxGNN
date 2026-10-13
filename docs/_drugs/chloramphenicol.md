---
layout: default
title: Chloramphenicol
parent: Evidencia Moderada (L3-L4)
nav_order: 151
evidence_level: L3
indication_count: 9
---

# Chloramphenicol
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **9** 
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

# Cloranfenicol: De Cloranfenicol (indicación registrada) a Conjuntivitis

## Resumen en Una Frase

Cloranfenicol es un antibiótico de amplio espectro cuyo registro sanitario en Colombia (CLORAFENICOL 250 MG, cápsula dura) figura únicamente con el nombre del principio activo como indicación aprobada, sin una enfermedad específica descrita.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis**, con **0 ensayos clínicos** y **20 publicaciones** relacionadas (principalmente revisiones, comentarios y reportes de casos).
Se trata de un uso ya establecido en formulaciones oftálmicas tópicas en varios países, más que de un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLORAMFENICOL (el registro no detalla una enfermedad específica) |
| Nueva Indicación Predicha | Conjuntivitis |
| Puntaje de Predicción TxGNN | 99,66% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el cloranfenicol es un antibiótico bacteriostático de amplio espectro que inhibe la subunidad ribosomal 50S bacteriana, bloqueando la síntesis de proteínas. Esto es compatible con su uso en infecciones bacterianas oculares.

La relación entre la indicación original y la nueva es directa: la conjuntivitis bacteriana es una infección superficial del ojo, y las preparaciones oftálmicas tópicas de cloranfenicol se usan desde hace décadas para tratarla, sobre todo en el Reino Unido, mientras que en EE. UU. se prescribe muy poco con este fin. Por ello, la predicción de TxGNN refleja un uso ya conocido, no un hallazgo nuevo.

Un punto importante es que el producto registrado en Colombia es una cápsula dura de uso sistémico, y no una formulación oftálmica. La compatibilidad de vía de administración con la nueva indicación sigue pendiente de evaluar y requeriría una formulación tópica oftálmica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32959365](https://pubmed.ncbi.nlm.nih.gov/32959365/) | 2020 | Revisión sistemática (Cochrane) | Cochrane Database of Systematic Reviews | Intervenciones para prevenir la oftalmía neonatal, infección ocular del recién nacido que puede causar ceguera |
| [38511104](https://pubmed.ncbi.nlm.nih.gov/38511104/) | 2024 | Estudio comparativo (diseño no confirmado) | Current Therapeutic Research | Compara moxifloxacino con cloranfenicol en infecciones oculares bacterianas |
| [3554881](https://pubmed.ncbi.nlm.nih.gov/3554881/) | 1987 | Comparativo aleatorizado, simple ciego | Acta Ophthalmologica | Ácido fusídico vs. cloranfenicol en conjuntivitis purulenta aguda: éxito clínico 84% vs. 81%; más molestias leves con cloranfenicol (14% vs. 5%) |
| [3300139](https://pubmed.ncbi.nlm.nih.gov/3300139/) | 1987 | Comparativo abierto aleatorizado | Acta Ophthalmologica | Ácido fusídico (93% de éxito) superó a cloranfenicol (48%) y framicetina (74%) en conjuntivitis bacteriana en Tanzania |
| [8800624](https://pubmed.ncbi.nlm.nih.gov/8800624/) | 1996 | Revisión de seguridad | Drug Safety | Debate sobre la posible relación entre cloranfenicol ocular tópico y anemia aplásica |
| [11270936](https://pubmed.ncbi.nlm.nih.gov/11270936/) | 2001 | Revisión | Drugs | Revisión comparativa de 16 preparaciones antibacterianas oftálmicas tópicas |
| [10589371](https://pubmed.ncbi.nlm.nih.gov/10589371/) | 1999 | Revisión | Clinical Pharmacokinetics | Tratamiento de infecciones oculares con antibacterianos tópicos |
| [7498557](https://pubmed.ncbi.nlm.nih.gov/7498557/) | 1995 | Revisión/Comentario | Eye | Uso y abuso del cloranfenicol tópico |
| [25833086](https://pubmed.ncbi.nlm.nih.gov/25833086/) | 2015 | Comentario | Clinical & Experimental Ophthalmology | Cloranfenicol de venta libre |
| [7153511](https://pubmed.ncbi.nlm.nih.gov/7153511/) | 1982 | Estudio clínico/laboratorio | The Journal of Hygiene | En conjuntivitis neonatal por clamidia, el cloranfenicol retrasó y atenuó los signos, pero el 85% de los lactantes tratados seguía con cultivo positivo |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19987544 (cancelado) | CLORAFENICOL 250 MG | Cápsula dura | CLORAMFENICOL |

---

## Citotoxicidad

No aplica la clasificación como antineoplásico; el cloranfenicol es un antibiótico, por lo que esta sección se omite.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: el modelo asocia el fármaco con contraindicación en enfermedades hematológicas (anemia aplásica, anemia, neutropenia y sus variantes congénitas, agranulocitosis, trombocitopenia, hemoglobinuria paroxística nocturna), enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, neuropatía periférica, neuritis óptica y porfiria aguda intermitente.
- **Advertencia clave**: la literatura recuperada discute un posible vínculo entre el cloranfenicol ocular tópico y la anemia aplásica, tema aún controvertido.
- **Interacciones Farmacológicas**: se identificaron 478 interacciones. Entre las de nivel **Mayor** figuran **cisaprida** y **naloxegol**. Entre las de nivel **Moderado** destacan metronidazol, sulfonilureas (clorpropamida, glimepirida, glipizida, gliburida, acetohexamida), repaglinida, saxagliptina, simvastatina, rosuvastatina, aprepitant, budesonida, hierro, balsalazida, eliglustat, naldemedina y nitisinona.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El uso del cloranfenicol tópico en conjuntivitis bacteriana está bien documentado en la literatura, incluidos comparativos aleatorizados antiguos, pero no hay ensayos clínicos registrados ni ECA de Fase 2/3 identificados, por lo que la evidencia se limita a L3. Además, el único registro sanitario en Colombia está cancelado y existe una señal de seguridad hematológica debatida.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA para advertencias y contraindicaciones oficiales.
- Confirmar el mecanismo de acción en DrugBank.
- Definir una formulación oftálmica tópica, ya que el producto registrado era una cápsula de uso sistémico.
- Aclarar las razones de la cancelación del registro y la situación regulatoria vigente.
- Evaluar la evidencia comparativa actual (por ejemplo, el estudio de 2024 con moxifloxacino) frente a alternativas disponibles.
- Establecer un plan de monitoreo hematológico y de minimización de riesgos.

---

### Otras indicaciones predichas (no recomendadas por ahora)

Las demás predicciones de TxGNN (esclerodermia difusa, vasculitis postinfecciosa, trastorno postbacteriano, síndrome postinfeccioso, estenosis uretral infecciosa, cardiomiopatía de Chagas, síndrome hemolítico urémico asociado a infección y queratoconjuntivitis epitelial punteada) tienen evidencia L4–L5 y decisión **Hold**. En varios casos los vínculos son artefactos de la predicción (por ejemplo, el uso del gen reportero CAT en estudios de esclerodermia) o carecen de plausibilidad mecanística, y el perfil de toxicidad hematológica del fármaco es una preocupación adicional.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

