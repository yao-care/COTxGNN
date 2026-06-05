---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Ravulizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ravulizumab: De Hemoglobinuria Paroxística Nocturna a Neutropenia Congénita Grave por Deficiencia de G6PC3

## Resumen en Una Frase

Ravulizumab es un anticuerpo monoclonal anti-C5 de larga duración, aprobado internacionalmente para el tratamiento de la hemoglobinuria paroxística nocturna (PNH) y el síndrome hemolítico urémico atípico (aHUS), cuya acción consiste en bloquear el componente terminal de la cascada del complemento.
El modelo TxGNN predice que podría ser efectivo para la **Neutropenia Congénita Grave de tipo autosómico recesivo por deficiencia de G6PC3**,
con **0 ensayos clínicos** y **0 publicaciones** que respalden actualmente esta dirección — la predicción se basa exclusivamente en señales del modelo.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Hemoglobinuria paroxística nocturna (PNH) / SHU atípico (referencia internacional; no registrado en Colombia) |
| Nueva Indicación Predicha | Neutropenia congénita grave AR por deficiencia de G6PC3 |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales de mecanismo de acción en el Evidence Pack. Con base en la información contextual presente en las racionalizaciones del modelo, Ravulizumab es un inhibidor del componente C5 del complemento: bloquea la escisión de C5 en C5a y C5b, impidiendo la formación del complejo de ataque a la membrana (MAC) y la liberación de C5a anafilatóxina. Su ventaja sobre eculizumab radica en una vida media más prolongada (administración cada 8 semanas), manteniendo supresión sostenida del complemento terminal.

La Neutropenia Congénita Grave AR por deficiencia de G6PC3 es un trastorno metabólico que compromete la subunidad catalítica 3 de la glucosa-6-fosfatasa, provocando acumulación de metabolitos tóxicos, estrés del retículo endoplásmico (ER stress) y apoptosis acelerada de los precursores de neutrófilos en la médula ósea. El modelo postula que la activación del complemento en el microambiente medular podría agravar el daño tisular, y que la inhibición de C5 ejercería un efecto protector indirecto sobre la maduración de los granulocitos.

Sin embargo, la conexión mecanística es extremadamente débil y no está respaldada por ningún dato experimental ni clínico. El puntaje elevado del modelo (99.96%) probablemente refleja efectos de agrupamiento topológico en el grafo de conocimiento: las múltiples subvariantes de neutropenia congénita grave comparten nodos de enfermedad, lo que genera puntuaciones altas por proximidad de grafo más que por relación farmacológica directa. La racionalización del propio sistema cataloga este hallazgo como posible **falso positivo por efecto de clúster de enfermedades raras**.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Ravulizumab no cuenta con registros sanitarios activos ante el INVIMA y no se encuentra comercializado en Colombia para ninguna indicación. Para poder avanzar con cualquier uso en el país sería necesario iniciar un proceso de registro sanitario o explorar vías de acceso excepcional (uso compasivo / importación por indicación médica).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya exclusivamente en señales del modelo TxGNN sin ningún ensayo clínico ni publicación de respaldo (Nivel de Evidencia L5), y el enlace mecanístico entre la inhibición de C5 y el ER stress por deficiencia de G6PC3 es teórico y muy débil — el elevado puntaje refleja muy probablemente proximidad topológica entre subtipos de neutropenia congénita en el grafo de conocimiento, no una relación farmacológica real.

**Para avanzar se necesita:**

- Datos formales de mecanismo de acción (MOA) de DrugBank para Ravulizumab, como prerrequisito para el análisis de relevancia mecanística
- Estudios preclínicos (modelos animales G6PC3-KO) que demuestren activación del complemento en el microambiente medular como parte de la patología
- Evidencia de biomarcadores de complemento (C3b, C5b-9/MAC) en pacientes diagnosticados con SCN por deficiencia de G6PC3
- Registro sanitario de Ravulizumab ante el INVIMA como prerrequisito regulatorio en Colombia
- Análisis de viabilidad económica: al ser un biológico de alto costo destinado a una enfermedad ultra-rara, cualquier desarrollo clínico requiere evaluación de costo-efectividad y exploración de mecanismos de acceso (fondos de enfermedades huérfanas, acuerdos con fabricante)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

