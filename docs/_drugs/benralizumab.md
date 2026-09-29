---
layout: default
title: Benralizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 86
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Benralizumab: De Asma Eosinofílica Grave a Trombocitopenia por Destrucción Inmune

## Resumen en Una Frase

Benralizumab es un anticuerpo monoclonal anti-IL-5Rα que se usa en enfermedades eosinofílicas, principalmente asma eosinofílica grave. El modelo TxGNN predice que podría ser efectivo para la **trombocitopenia por destrucción inmune**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Por ahora es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro sanitario (solo figura el principio activo). Uso conocido: asma eosinofílica grave |
| Nueva Indicación Predicha | Trombocitopenia por destrucción inmune |
| Puntaje de Predicción TxGNN | 99.34% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Benralizumab se une al receptor alfa de la IL-5 y elimina eosinófilos y basófilos mediante citotoxicidad celular dependiente de anticuerpos (ADCC). Por eso se usa en enfermedades donde los eosinófilos tienen un papel central. No hay datos de mecanismo de acción cargados en DrugBank para este registro, así que esta descripción proviene de la evaluación mecanística del propio paquete de evidencia.

La trombocitopenia inmune se debe a autoanticuerpos contra las plaquetas y a su depuración por macrófagos, con participación de linfocitos B y T. No se conoce un vínculo establecido entre esa vía y el bloqueo de IL-5Rα. Por eso el puntaje alto de TxGNN no tiene hoy un respaldo mecanístico plausible. Puede reflejar asociaciones del grafo de conocimiento y no una relación biológica real.

Entre las otras predicciones del modelo, **dermatitis** (posición 2) sí tiene evidencia. Un ensayo Fase 2 aleatorizado (HILLIER, publicado en 2023) mostró falta de efecto en dermatitis atópica moderada a grave, aunque una biopsia de piel confirmó que el fármaco depleta las células objetivo. Es un resultado negativo que no apoya el reposicionamiento en esa indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20145261 | FASENRA® (AstraZeneca Colombia S.A.S) | Solución inyectable | El registro solo indica el principio activo (Benralizumab), sin texto de indicación |

Nota: el listado devuelve entradas repetidas del mismo registro (20145261), por lo que se muestra una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos ni publicaciones que la respalden (nivel L5), y no hay un vínculo mecanístico entre la depleción de eosinófilos y la destrucción inmune de plaquetas. No hay base para avanzar.

**Para avanzar se necesita:**
- Una revisión sistemática de literatura sobre anti-IL-5/IL-5Rα en trombocitopenia inmune, para descartar señales clínicas o mecanísticas no detectadas.
- Datos de mecanismo de acción desde DrugBank.
- El prospecto de INVIMA con advertencias y contraindicaciones, para el tamizaje de seguridad.
- Una hipótesis biológica concreta que conecte IL-5Rα con la trombocitopenia inmune antes de considerar cualquier estudio.
- Como línea de investigación aparte, seguir el ensayo NCT06734884 (DRESS, Fase 2, aún sin reclutar), que estudia una condición cutánea eosinofílica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

