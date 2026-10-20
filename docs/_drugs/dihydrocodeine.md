---
layout: default
title: Dihydrocodeine
parent: Solo Predicción del Modelo (L5)
nav_order: 221
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Dihydrocodeine: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L5). Indicación original: DIHIDROCODEINA"
monitor_inn: "dihydrocodeine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "allergic urticaria", "papillary conjunctivitis", "faucial diphtheria", "cervical disc degenerative disorder", "headache disorder", "cold urticaria", "trigeminal autonomic cephalalgia"]
---

# Dihydrocodeine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Dihidrocodeína: De Dihidrocodeína (indicación sin especificar) a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

La dihidrocodeína es un analgésico opioide con actividad antitusiva; en Colombia contaba con registros sanitarios cuyo texto de indicación solo dice "DIHIDROCODEINA", sin detallar el uso aprobado.
El modelo TxGNN predice que podría ser efectiva para **enfermedad de la cavidad nasal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción: es únicamente una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DIHIDROCODEINA (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin productos vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la dihidrocodeína es un opioide con efectos antitusivos y analgésicos. Mecanísticamente, un vínculo con afecciones de las vías respiratorias superiores es concebible, pero solo como alivio sintomático.

El puntaje de TxGNN es muy alto (99.99%), pero es una predicción computacional. Los datos compilados para este informe no contienen ensayos ni literatura que sustenten una relación entre el fármaco y las enfermedades de la cavidad nasal. La similitud con la indicación original no ha sido evaluada.

Otras predicciones del modelo (por ejemplo, laringofaringitis aguda, cefalea, enfermedad degenerativa del disco cervical) tienen igualmente un respaldo muy limitado. En urticaria alérgica y urticaria por frío, el vínculo plausible apunta más a un posible daño que a un beneficio, porque los opioides pueden liberar histamina.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicación principal (enfermedad de la cavidad nasal) actualmente no hay literatura relacionada disponible.

Como referencia, para la predicción de rango 7 (trastorno de cefalea) se recuperaron dos publicaciones indirectas, que no aportan evidencia de eficacia:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11915306](https://pubmed.ncbi.nlm.nih.gov/11915306/) | 2002 | Estudio clínico | Nihon Arukoru Yakubutsu Igakkai zasshi | Tres casos de abuso de un jarabe antitusivo en Japón; productos previos con dihidrocodeína generaron dependencia |
| [28521551](https://pubmed.ncbi.nlm.nih.gov/28521551/) | 2017 | Revisión | J Pain Palliat Care Pharmacother | Resumen general de revisiones Cochrane, sin evidencia directa sobre dihidrocodeína |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 31398 | PARACODINA JARABE | Jarabe | DIHIDROCODEINA (cancelado) |
| 19955900 | DIHIDROCODEINA BITARTRATO 2.42 MG/ML JARABE | Jarabe | DIHIDROCODEINA (cancelado) |
| 33722 | PARACODINA GOTAS | Solución oral | DIHIDROCODEINA (cancelado) |
| 20056688 | DIHIDROCODEINA 2.42 MG/ML SOLUCIÓN ORAL | Solución oral | DIHIDROCODEINA (cancelado) |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento del modelo asocia el fármaco con contraindicaciones en múltiples condiciones, entre ellas: insuficiencia hepática y enfermedad hepática, enfermedad renal, EPOC, epilepsia, pancreatitis, enfermedad de la vesícula biliar, hipotiroidismo/mixedema, úlcera péptica, enfermedad inflamatoria intestinal, diabetes y cetoacidosis diabética, hiperplasia prostática benigna, hipertensión e hipotensión, gota, abuso/dependencia de sustancias, hemofilia, trombocitopenia, enfermedad coronaria e infarto de miocardio, hemoglobinopatías e insomnio.
- **Interacciones farmacológicas:** se identificaron 119 interacciones; entre las de nivel **mayor** figuran **alvimopán** y **bupropión**. Entre las de nivel moderado destacan anticolinérgicos (atropina, diciclomina, glicopirronio, hiosciamina), antidiarreicos (loperamida, caolín, atapulgita), antieméticos (aprepitant, granisetrón, dolasetrón), cimetidina, dexametasona, dronabinol y eluxadolina.
- Como clase, los opioides conllevan riesgo de dependencia, abuso, depresión respiratoria y cefalea por abuso de medicación. La información de advertencias y contraindicaciones del prospecto no está disponible; consultar el prospecto de INVIMA.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y no existen productos vigentes en Colombia. Además, el perfil de riesgo de un opioide (dependencia, interacciones mayores, múltiples contraindicaciones) exige una justificación clínica sólida que hoy no existe.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Aclarar la indicación original real de los registros cancelados y el motivo de su cancelación.
- Realizar una revisión sistemática de la literatura sobre dihidrocodeína en enfermedades de la cavidad nasal y vías respiratorias superiores.
- Evaluar la compatibilidad de vías de administración y la relación riesgo-beneficio frente a alternativas establecidas.
- Considerar si otras predicciones (por ejemplo, laringofaringitis aguda) tienen una justificación sintomática más clara antes de priorizar esta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

