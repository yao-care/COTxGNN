---
layout: default
title: Risperidone
parent: Solo Predicción del Modelo (L5)
nav_order: 346
evidence_level: L5
indication_count: 6
---

# Risperidone
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

# Risperidona: De Esquizofrenia a Síndrome de Parálisis de la Mirada Horizontal Familiar con Escoliosis Progresiva

## Resumen en Una Frase

La risperidona es un antipsicótico atípico, usado originalmente para la esquizofrenia, los episodios maníacos del trastorno bipolar y la irritabilidad en el autismo.
El modelo TxGNN predice que podría ser efectiva para **parálisis de la mirada horizontal familiar con escoliosis progresiva**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El texto del registro INVIMA solo dice "RISPERIDONA", sin indicación. Según la fuente farmacológica: esquizofrenia, manía bipolar e irritabilidad en autismo |
| Nueva Indicación Predicha | Parálisis de la mirada horizontal familiar con escoliosis progresiva |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el campo MOA de DrugBank. Los datos farmacológicos indican que la risperidona actúa sobre receptores de serotonina (5-HT1A, 1B, 1D, 1E, 1F, 2A, 2C, 6 y 7), adrenérgicos (α1A, α1B, α1D y α2A), de dopamina (D2 y D3) y de histamina H1. Su efecto antipsicótico se atribuye sobre todo al bloqueo de D2 y 5-HT2A.

La nueva indicación es un trastorno estructural del neurodesarrollo, extremadamente raro. No hay un vínculo mecanístico con el bloqueo de D2/5-HT2A ni evidencia que lo respalde. La única señal es el puntaje alto del modelo, por lo que esta predicción no es razonable sin evidencia adicional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20007289 | RISPERIDONA 2 MG (Tecnoquímicas S.A.) | Tableta cubierta (gragea) | RISPERIDONA (sin texto de indicación) |

Las cinco entradas devueltas corresponden al mismo registro, por lo que se muestra una sola vez. Hay además una forma "tableta recubierta" por vía oral. El paquete de evidencia reporta 20 registros en total.

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: los 16 registros de "interacciones" del paquete son en realidad datos de afinidad por receptores (perfil farmacológico), no interacciones con otros fármacos. Los blancos son los receptores serotoninérgicos, adrenérgicos, dopaminérgicos e histamínicos mencionados arriba. Una posible consecuencia práctica es el efecto aditivo con otros depresores del sistema nervioso central o antihipertensivos.

Consultar el prospecto para advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5), sin ensayos, sin literatura y sin mecanismo plausible para un trastorno tan raro.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es una brecha bloqueante.
- Completar el MOA desde DrugBank.
- Revisar la evidencia antes de cualquier evaluación clínica. Dentro del mismo paquete, el trastorno afectivo mayor (rango 6, puntaje 99.11%) tiene nivel L1: varios ensayos de Fase 3 completados y metaanálisis de aumento con antipsicóticos en depresión resistente y bipolar. Se recomienda evaluarlo en un informe aparte, con barandillas (Proceed with Guardrails): poblaciones resistentes o bipolares, y monitoreo metabólico, de prolactina y de síntomas extrapiramidales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

