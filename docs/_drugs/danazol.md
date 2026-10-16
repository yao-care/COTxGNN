---
layout: default
title: Danazol
parent: Evidencia Moderada (L3-L4)
nav_order: 193
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Danazol: nueva indicación predicha, Amenorrea (nivel de evidencia L3). Indicación original: DANAZOL"
---

# Danazol
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

# Danazol: De Indicación Original (Danazol) a Amenorrea

## Resumen en Una Frase

Danazol es un esteroide sintético con actividad androgénica y antigonadotrópica; en Colombia su único registro sanitario (hoy cancelado) lo identifica solo como "DANAZOL", sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, aunque la propia lógica farmacológica indica que el fármaco *induce* amenorrea en lugar de tratarla.
La predicción cuenta con **0 ensayos clínicos** y **20 publicaciones** (en su mayoría revisiones y estudios antiguos), por lo que la evidencia es limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DANAZOL (el registro no especifica una indicación clínica) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99,9995 % |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin comercialización vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Danazol es un esteroide sintético derivado de la 17α-etiniltestosterona. Suprime las gonadotropinas hipofisarias (LH/FSH) y la esteroidogénesis ovárica, lo que produce atrofia endometrial y amenorrea. Los datos compilados para este informe no incluyen un mecanismo de acción formal, pero la literatura revisada describe estos efectos.

Aquí hay una salvedad importante: la relación entre la indicación original y la nueva no es la habitual. Danazol ya se usa para **inducir** amenorrea (supresión menstrual en endometriosis, sangrado uterino anormal y atención a personas transgénero). Tratar una amenorrea patológica ya existente es distinto, porque el fármaco provoca la condición en lugar de revertirla. El puntaje alto de TxGNN probablemente refleja este efecto inductor de amenorrea y no un beneficio terapéutico para quienes ya la padecen.

Por ello, la plausibilidad mecanística es débil para el uso propuesto. Una reformulación más coherente sería "supresión menstrual terapéutica", no "tratamiento de la amenorrea".

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (prioridad: revisión sistemática/cohorte/comparativos > revisiones > otros).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39051650](https://pubmed.ncbi.nlm.nih.gov/39051650/) | 2024 | Cohorte retrospectiva | Women's Health | Uso de danazol para supresión menstrual en personas transgénero; induce amenorrea con efectos androgénicos reversibles |
| [36434439](https://pubmed.ncbi.nlm.nih.gov/36434439/) | 2023 | Revisión sistemática | Arch Gynecol Obstet | Seguridad y eficacia de gestrinona en endometriosis (fármaco comparable; induce atrofia endometrial/amenorrea) |
| [2523321](https://pubmed.ncbi.nlm.nih.gov/2523321/) | 1989 | Comparación clínica | Fertil Steril | Gestrinona vs. danazol en endometriosis (39 pacientes, 6 meses) |
| [2140996](https://pubmed.ncbi.nlm.nih.gov/2140996/) | 1990 | Doble ciego aleatorizado | Fertil Steril | Nafarelina vs. danazol en endometriosis (82 pacientes); ambos lograron regresión significativa de la enfermedad activa |
| [6210867](https://pubmed.ncbi.nlm.nih.gov/6210867/) | 1982 | Doble ciego | Obstet Gynecol | Danazol a 100–600 mg/día en endometriosis (27 mujeres); la mejoría clínica varió según la dosis |
| [2404115](https://pubmed.ncbi.nlm.nih.gov/2404115/) | 1990 | Revisión | J Reprod Med | Danazol inhibe gonadotropinas y esteroidogénesis y tiene efectos inmunorreguladores |
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Revisión | Menopause | Tratamientos farmacológicos del sangrado uterino anormal |
| [16280355](https://pubmed.ncbi.nlm.nih.gov/16280355/) | 2006 | Revisión | Hum Reprod Update | Manejo de la endometriosis; las lesiones regresan en estados de amenorrea o menopausia |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Revisión | J R Army Med Corps | Inducción terapéutica de amenorrea en personal femenino movilizado |
| [2013670](https://pubmed.ncbi.nlm.nih.gov/2013670/) | 1991 | Encuesta clínica | J Allergy Clin Immunol | Andrógenos atenuados en angioedema hereditario; dosis eficaces de danazol ≤200 mg/día e irregularidades menstruales como efecto adverso |

Ninguna publicación evalúa danazol como tratamiento de la amenorrea patológica.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19905582 | CIPLADANOGEN® 200 MG CÁPSULAS | Cápsula dura | DANAZOL | Cancelado |

---

## Consideraciones de Seguridad

Los datos de advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto para esa información. Se dispone de la siguiente información complementaria:

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto):** epilepsia, porfiria (incluida la hereditaria) y otros trastornos del metabolismo de porfirinas, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, carcinoma de mama femenino, migraña e hiperlipidemia familiar combinada.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Las principales son:
  - **Mayor:** cisaprida.
  - **Moderadas:** antidiabéticos (acarbosa, albiglutida, alogliptina, canagliflozina, clorpropamida, acetohexamida, dapagliflozina, dulaglutida, empagliflozina, ertugliflozina, exenatida, glimepirida, glipizida, gliburida, insulinas), budesonida (incluida la nasal) y eliglustat.
- **Señales adicionales de la literatura:** el aumento de las concentraciones de carbamazepina con danazol (PMID 3107168) y un caso de rabdomiólisis y pancreatitis con lovastatina (PMID 18691993).
- **Efectos androgénicos:** cambios de voz y vello, descritos en la cohorte de supresión menstrual.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es coherente con el efecto farmacológico conocido, pero este es inductor de amenorrea, no correctivo. No hay ensayos clínicos ni evidencia de beneficio en amenorrea patológica. Además, el único registro colombiano está cancelado y el perfil de seguridad es relevante (androgénico, hepático, interacciones).

**Para avanzar se necesita:**
- Definir si la pregunta real es la supresión menstrual (reformular la indicación) y no el tratamiento de la amenorrea.
- Obtener el prospecto con advertencias y contraindicaciones oficiales.
- Obtener datos del mecanismo de acción desde DrugBank.
- Evaluar la disponibilidad actual de danazol en Colombia, dado que el registro está cancelado.
- Generar evidencia clínica controlada, ya que hoy solo existen revisiones y estudios antiguos.

### Otras indicaciones predichas (referencia)

Dentro de los datos compilados, la **displasia mamaria benigna** (puntaje 99,999 %, nivel L3, con ensayos doble ciego aleatorizados antiguos) y la **adenosis mamaria** (L3) presentan mayor respaldo clínico que la amenorrea, por lo que podrían ser mejores candidatas para una evaluación más profunda. Las demás (adenosis apocrina, adenosis de conductos romos, absceso mamario, necrosis grasa, enfermedad de la lactancia, vulvovaginitis, vulvitis) tienen evidencia indirecta o nula (L4–L5) y se recomienda mantenerlas en espera.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

