---
layout: default
title: Ramucirumab
parent: Solo Predicción del Modelo (L5)
nav_order: 547
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ramucirumab: nueva indicación predicha, Adenocarcinoma del ligamento uterino (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo indica \"RAMUCI…"
monitor_inn: "RAMUCIRUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament clear cell adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Ramucirumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Ramucirumab: De Indicación No Especificada en el Registro a Adenocarcinoma del Ligamento Uterino
{: .text-alpha }

## Resumen en Una Frase

Ramucirumab es un anticuerpo monoclonal comercializado como CYRAMZA®, cuyo registro sanitario en Colombia no detalla la indicación original (solo repite el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para **adenocarcinoma del ligamento uterino**, con un puntaje muy alto.
Actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección, por lo que la evidencia se limita a la predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "RAMUCIRUMAB") |
| Nueva Indicación Predicha | Adenocarcinoma del ligamento uterino |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen el mecanismo de acción detallado. Según el conocimiento general (no proveniente de los datos suministrados), ramucirumab es un antagonista del receptor 2 del factor de crecimiento endotelial vascular (VEGFR-2). Al bloquear esta vía se inhibe la angiogénesis, un proceso del que dependen muchos tumores sólidos para crecer.

Los adenocarcinomas de origen ginecológico pueden depender de la señalización VEGF, por lo que existe una justificación teórica para el bloqueo de VEGFR-2. Sin embargo, esta relación se basa únicamente en el puntaje alto de TxGNN y en conocimiento general: no se suministraron ensayos ni literatura para esta indicación, y la similitud con la indicación original no pudo evaluarse porque esta no está detallada.

### Otras indicaciones predichas (todas con evidencia L5 y recomendación Hold)

| Posición | Enfermedad predicha | Puntaje TxGNN |
|------|------|------|
| 2 | Carcinoma endocervical | 0.9995 |
| 3 | Carcinoma adenoide quístico del cuello uterino | 0.9995 |
| 4 | Adenocarcinoma seroso del ligamento uterino | 0.9994 |
| 5 | Adenocarcinoma mucinoso cervical, variante de células en anillo de sello | 0.9994 |
| 6 | Carcinoma adenoescamoso cervical, variante de células vítreas | 0.9994 |
| 7 | Adenocarcinoma endometrioide del ligamento uterino | 0.9994 |
| 8 | Adenocarcinoma de células claras del ligamento uterino | 0.9994 |
| 9 | Adenocarcinoma mucinoso del ligamento uterino | 0.9994 |
| 10 | Adenocarcinoma mucinoso cervical, variante intestinal | 0.9994 |

Todas comparten la misma limitación: justificación mecanística teórica sin estudios de respaldo en los datos compilados.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20111011 (cancelado) | CYRAMZA® (ELI LILLY & COMPANY) | Solución concentrada para infusión | RAMUCIRUMAB (sin detalle de indicación) |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-VEGFR-2), según conocimiento general |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en general, presión arterial, proteinuria y hemograma |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones; se muestran las 20 primeras de la consulta. Las de nivel **mayor** incluyen:
  - Ácido acetilsalicílico
  - Deferasirox
  - Ibritumomab tiuxetán
  - Tositumomab (con y sin I-131)
  - Anticoagulantes y antiagregantes: abciximab, alteplasa, antitrombina III humana, apixabán, betrixabán, bivalirudina, cangrelor, caplacizumab, cilostazol, clopidogrel, dalteparina y defibrótido

  Las de nivel **moderado** incluyen dexfenfluramina, fenfluramina y sibutramina. En conjunto, predominan las interacciones relacionadas con el riesgo de sangrado.

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje de TxGNN (nivel L5), sin ensayos clínicos ni literatura. Además, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones (brecha bloqueante)
- Confirmar el mecanismo de acción desde DrugBank
- Aclarar la indicación original aprobada y el motivo de la cancelación del registro
- Buscar estudios preclínicos, ensayos clínicos y literatura para la indicación predicha
- Evaluar la compatibilidad de la vía de administración (infusión intravenosa) y la similitud con la indicación original
- Revisar el riesgo hemorrágico por las interacciones mayores con anticoagulantes y antiagregantes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

