---
layout: default
title: Calcitriol
parent: Solo Predicción del Modelo (L5)
nav_order: 128
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Calcitriol: nueva indicación predicha, Deficiencia de vitamina D (término obsoleto) (nivel de evidencia L5). Indicación original: No detallada"
---

# Calcitriol
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

# Calcitriol: De una Indicación No Detallada en el Registro a Deficiencia de Vitamina D (término obsoleto)

## Resumen en Una Frase

Calcitriol es la forma activa de la vitamina D. En Colombia sus registros sanitarios solo indican "Calcitriol" como indicación, sin detallar para qué enfermedad se aprobó.
El modelo TxGNN predice que podría ser efectivo para **deficiencia de vitamina D (término obsoleto)**, pero **no hay ensayos clínicos ni publicaciones** que respalden específicamente esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada (el registro solo indica "Calcitriol") |
| Nueva Indicación Predicha | Deficiencia de vitamina D (término obsoleto) |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, calcitriol es la forma activa de la vitamina D, por lo que existe un vínculo biológico plausible con la deficiencia de vitamina D.

Sin embargo, el término de la enfermedad está marcado como **obsoleto**, es decir, es una entrada de ontología en desuso. El puntaje alto probablemente refleja un artefacto de nomenclatura y no una indicación nueva y accionable. No se aportaron ensayos ni literatura que lo respalden.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Los dos registros sanitarios están **cancelados**; no hay registros vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19934690 | Calcitriol 0.25 mcg cápsula blanda (COLMED LTDA) | Cápsula blanda | Calcitriol |
| 19942545 | Calcitriol 0.5 mcg (COLMED LTDA) | Cápsula blanda | Calcitriol |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN, no texto de prospecto): enfermedad renal, piouréter, sarcoidosis, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, susceptibilidad a nefrolitiasis por SLC26A1, nefrolitiasis, nefropatía aguda por uratos, hiperfosfatemia, hipervitaminosis y arteriosclerosis obliterante.
- **Interacciones farmacológicas**: se registraron 100 interacciones. Entre las principales:
  - **Mayores**: colecalciferol, burosumab y calcifediol.
  - **Moderadas**: fosfenitoína, hidroclorotiazida, amobarbital, butalbital, butabarbital, carbamazepina, calcipotriol tópico, hidróxido de aluminio, tiazidas y similares (bendroflumetiazida, benztiazida, clorotiazida, clortalidona), resinas de unión a ácidos biliares (colestiramina, colesevelam, colestipol) y glucósidos digitálicos (digitoxina, digoxina).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal se apoya solo en el modelo (L5), sin ensayos ni literatura, y corresponde a un término de enfermedad obsoleto. Además, los dos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Reemplazar el término obsoleto por la entidad vigente y verificar si la predicción aporta una indicación distinta de las ya conocidas.
- Obtener el mecanismo de acción detallado y las advertencias y contraindicaciones del prospecto en INVIMA.
- Evaluar la reactivación o nueva solicitud de registro, dado que no hay productos vigentes.

**Nota sobre otras predicciones del mismo fármaco:**
Entre las demás predicciones, la **hipofosfatemia raquítica hereditaria** (puntaje 99.28%) tiene el mayor respaldo: nivel L3 y recomendación *Proceed with Guardrails*. Cuenta con 2 ensayos clínicos: uno de Fase temprana 1, completado, con 16 participantes, sobre calcitriol en monoterapia en hipofosfatemia ligada al X; y uno de Fase 4, de estado desconocido, con 100 participantes, que compara dosis de vitamina D activa más fosfato. También cuenta con múltiples revisiones que describen calcitriol más fosfato como tratamiento estándar. Requiere vigilar hipercalciuria, nefrocalcinosis e hiperparatiroidismo. La **acidosis tubular renal** tiene nivel L4, con evidencia solo fisiológica y de casos, sin evidencia de que calcitriol trate la acidosis en sí.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

