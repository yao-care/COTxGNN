---
layout: default
title: Belimumab
parent: Solo Predicción del Modelo (L5)
nav_order: 84
evidence_level: L5
indication_count: 6
---

# Belimumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Belimumab: De Lupus Eritematoso Sistémico a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Belimumab es un anticuerpo monoclonal anti-BLyS (BAFF) que se comercializa en Colombia como Benlysta (GlaxoSmithKline). Su uso conocido es el lupus eritematoso sistémico, aunque el registro INVIMA del paquete de datos solo consigna el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria**, con **1 ensayo clínico** de baja relevancia y **ninguna publicación** que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lupus eritematoso sistémico (indicación conocida del fármaco; en el registro INVIMA el texto aprobado dice solamente «BELIMUMAB») |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Belimumab es un anticuerpo monoclonal anti-BLyS (BAFF) que reduce la supervivencia de los linfocitos B y la producción de autoanticuerpos. Ese mecanismo es el que sustenta su uso en enfermedades autoinmunes mediadas por anticuerpos.

Los trastornos primarios de liberación plaquetaria son, sobre todo, defectos intrínsecos de los gránulos o de la señalización plaquetaria. No son enfermedades autoinmunes, así que no hay un vínculo mecanístico claro con la inhibición de linfocitos B. El puntaje TxGNN muy alto (0.9996) proviene de patrones del grafo de conocimiento y no de biología que lo respalde. La única vía concebible sería una variante autoinmune adquirida, sin datos que la sostengan.

Entre las otras predicciones del modelo, la más coherente biológicamente es la **trombocitopenia aloinmune fetal y neonatal (FNAIT)**. Sus aloanticuerpos maternos (principalmente anti-HPA-1a) podrían, en teoría, reducirse con la modulación de linfocitos B y células plasmáticas. Sin embargo, el uso en embarazo tiene datos de seguridad limitados y hay transferencia placentaria de IgG. El estándar actual es la inmunoglobulina intravenosa, con o sin corticosteroides. No existe evidencia clínica, así que sigue siendo solo una hipótesis. Las demás predicciones (pseudo-enfermedad de von Willebrand, trombastenia de Glanzmann, macrotrombocitopenia autosómica dominante, retinopatía diabética no proliferativa severa) carecen de sustento biológico.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Fase 2 | Completado | 14 | Estudio mecanístico abierto de belimumab en glomerulonefropatía membranosa idiopática con autoanticuerpos anti-PLA2R positivos. Es otra enfermedad, sin relación con los trastornos plaquetarios. Se calificó con relevancia C y probablemente es una coincidencia espuria de la búsqueda. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20048122 | BENLYSTA 120 MG POLVO LIOFILIZADO CONCENTRADO PARA SOLUCION PARA INFUSION (GlaxoSmithKline Colombia S.A.) | Polvo liofilizado para reconstituir a solución inyectable | BELIMUMAB (el registro no detalla el texto de la indicación) |

Nota: las 5 entradas del paquete de datos corresponden al mismo registro sanitario y se presentan aquí una sola vez.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal tiene un puntaje TxGNN muy alto, pero no cuenta con ningún estudio real ni base mecanística: el único ensayo asociado es de otra enfermedad y de relevancia baja. Las 6 predicciones están en nivel L5, y solo la FNAIT merece considerarse como pregunta de investigación.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones, que es un vacío de datos bloqueante para el tamizaje de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank para el análisis mecanístico formal.
- Revisar la literatura sobre belimumab y otros agentes anti-BAFF en trombocitopenias inmunes o aloinmunes, y evaluar la FNAIT como hipótesis.
- Analizar la seguridad en el embarazo antes de cualquier consideración en FNAIT.
- Descartar por ahora las demás predicciones, salvo que aparezca evidencia nueva.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

