---
layout: default
title: Norfloxacin
parent: Solo Predicción del Modelo (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
---

# Norfloxacin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Norfloxacina: De Antibacteriano (indicación no detallada en el registro) a Hiperamilasemia

## Resumen en Una Frase

Norfloxacina es una fluoroquinolona antibacteriana comercializada en Colombia en tabletas de 400 mg. Los registros sanitarios solo citan el nombre del principio activo, sin describir la indicación.
El modelo TxGNN predice que podría ser efectiva para **hiperamilasemia**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | NORFLOXACINA (el registro solo indica el nombre del principio activo, sin texto de indicación) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de la norfloxacina en el Evidence Pack. Por su clase (fluoroquinolona), se sabe que inhibe la ADN girasa y la topoisomerasa IV bacterianas. Su eficacia antibacteriana es conocida, pero las indicaciones originales no están documentadas en los datos recibidos.

La hiperamilasemia es un hallazgo de laboratorio (amilasa elevada en sangre), no una enfermedad con una diana antibacteriana. No se identificó ningún vínculo mecanístico entre inhibir enzimas bacterianas y normalizar la amilasa sérica.

El puntaje de 99.70% proviene solo de patrones del grafo de conocimiento de TxGNN. Sin ensayos, literatura ni mecanismo plausible, esta predicción no es más que una hipótesis del modelo. Es probable que sea un artefacto del grafo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Hay 20 registros sanitarios en total. Los datos recibidos muestran estos productos distintos (algunas entradas aparecen repetidas):

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 29749 | NORFLOXACINA 400MG (Tecnoquímicas S.A.) | Tableta cubierta (gragea) | NORFLOXACINA |
| 19942965 | UROTRIN® 400 MG TABLETAS (Bioquifar Pharmaceutica S.A.) | Tableta recubierta | NORFLOXACINA |

Otras formas farmacéuticas registradas: tableta y cápsula dura.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos, literatura ni mecanismo plausible (nivel L5). Además, la hiperamilasemia es un hallazgo de laboratorio y no un objetivo terapéutico antibacteriano. No se recomienda avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Prospecto de INVIMA con advertencias y contraindicaciones, que hoy es un vacío bloqueante para el tamizaje de seguridad.
- Aclarar las indicaciones originales aprobadas, porque los registros solo citan el nombre del principio activo.
- Una definición clínica de qué significaría "tratar" la hiperamilasemia: ¿la causa subyacente o solo el valor de laboratorio?
- Como alternativa, revisar las otras predicciones con algo de literatura. Queda en "Pregunta de Investigación" la queratoconjuntivitis epitelial punteada (2 estudios sobre queratoconjuntivitis microsporidial que no mencionan norfloxacina) y la peste septicémica (un estudio experimental de profilaxis con fluoroquinolonas que no nombra norfloxacina). Ambas requieren revisión de texto completo y de farmacocinética antes de avanzar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

