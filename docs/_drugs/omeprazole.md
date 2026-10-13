---
layout: default
title: Omeprazole
parent: Evidencia Moderada (L3-L4)
nav_order: 485
evidence_level: L3
indication_count: 2
---

# Omeprazole
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **2** 
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

# Omeprazol: De Indicación Original (Omeprazol) a Reflujo Duodenogástrico

## Resumen en Una Frase

Omeprazol es un inhibidor de la bomba de protones que suprime la secreción de ácido gástrico; en sus registros sanitarios colombianos figura únicamente con el nombre del principio activo como indicación.
El modelo TxGNN predice que podría ser efectivo para **reflujo duodenogástrico**, con **1 ensayo clínico** (solo de contexto indirecto) y **15 publicaciones** relacionadas, aunque ninguna demuestra de forma directa su eficacia en esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | OMEPRAZOL (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Reflujo duodenogástrico |
| Puntaje de Predicción TxGNN | 99.64% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, omeprazol inhibe la bomba de protones gástrica (H+/K+ ATPasa, codificada por el gen ATP4A), y su eficacia en enfermedades relacionadas con el exceso de ácido, como el reflujo gastroesofágico, está bien establecida.

El reflujo duodenogástrico consiste en el paso de bilis y jugo pancreático del duodeno al estómago. Su causa principal no es el ácido, por lo que suprimir el ácido no ataca directamente el origen del problema. Aun así, omeprazol podría aliviar síntomas y lesiones de la mucosa asociados al ácido en cuadros de reflujo mixto, como el esófago de Barrett. Algunos estudios clínicos pequeños evaluaron su efecto sobre el reflujo biliar en ese contexto.

Hay además una señal de precaución. Estudios preclínicos en ratas (PMID 10389684 y 8943968) sugieren que el bloqueo ácido, en presencia de reflujo duodenogástrico, podría estimular el crecimiento de la mucosa y favorecer la carcinogénesis gástrica. El puntaje TxGNN es una predicción computacional y no sustituye la evidencia clínica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | No aplica | Completado | 157 | Imagen endoscópica trimodal para distinguir dispepsia funcional de enfermedad por reflujo (ácido o biliar). Es un estudio diagnóstico que no evalúa omeprazol; relevancia solo contextual. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Estudio clínico | Scand J Gastroenterol | Efecto de omeprazol sobre el reflujo duodenogástrico antral en esófago de Barrett. |
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Estudio clínico | Gut | Efecto de omeprazol 20 mg dos veces al día sobre el reflujo biliar duodenogástrico y gastroesofágico en esófago de Barrett. |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Estudio prospectivo | J Pediatr Gastroenterol Nutr | Resultados de omeprazol en reflujo biliar esofágico en niños. |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Serie de casos | Eur J Pediatr | Reflujo duodenogástrico primario en seis niños y adolescentes, con síntomas que no respondían a antiácidos. |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revisión | Eur J Clin Pharmacol | Actualización del uso clínico y la farmacocinética de los inhibidores de la bomba de protones. |
| [8076761](https://pubmed.ncbi.nlm.nih.gov/8076761/) | 1994 | Estudio clínico | Gastroenterology | Relación entre pH, reflujo duodenogastroesofágico y esófago de Barrett. |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Estudio animal | Acta Cir Bras | Omeprazol y adenocarcinoma gástrico en ratas con reflujo duodenogástrico; se investiga un posible efecto protector. |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Estudio animal | Dig Dis Sci | El bloqueo ácido con omeprazol promovió la carcinogénesis gástrica inducida por reflujo duodenogástrico. |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Estudio animal | Dig Dis Sci | El reflujo duodenogástrico estimula el crecimiento de la mucosa, potenciado por el bloqueo ácido. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20066112 | OMEPRAZOL 40 MG (COLMED LTDA) – cancelado | Cápsula dura | OMEPRAZOL |
| 20066115 | OMEPRAZOL 20 MG (PROCAPS S.A.) – cancelado | Cápsula dura | OMEPRAZOL |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, osteoporosis, osteoporosis posmenopáusica, fractura ósea y gastritis atrófica crónica.
- **Interacciones y dianas farmacológicas:** se identificaron 2 registros de farmacología, con la bomba de protones gástrica (ATP4A) y el canal de cloruro ClC-2 (CLCN2). Corresponden a dianas moleculares y no a interacciones medicamentosas clínicas con nivel de gravedad.
- **Señal preclínica:** en modelos de rata, el bloqueo ácido con omeprazol potenció el crecimiento de la mucosa y la carcinogénesis en presencia de reflujo duodenogástrico.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos que prueben omeprazol en reflujo duodenogástrico. La evidencia se limita a estudios pequeños en esófago de Barrett y a modelos animales que sugieren un posible riesgo. Además, el mecanismo del fármaco (supresión ácida) no aborda la causa principal del reflujo biliar, y actualmente no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y análisis de su vínculo mecanístico con la nueva indicación.
- Ensayos clínicos controlados que evalúen omeprazol en reflujo duodenogástrico, con desenlaces de síntomas y exposición biliar.
- Evaluación de la señal de carcinogénesis observada en modelos animales.
- Obtener y revisar el prospecto de INVIMA para completar el tamizaje de seguridad.
- Aclarar la situación regulatoria, ya que los dos registros sanitarios están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

