---
layout: default
title: Panitumumab
parent: Solo Predicción del Modelo (L5)
nav_order: 316
evidence_level: L5
indication_count: 2
---

# Panitumumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Panitumumab: De Anticuerpo Anti-EGFR (indicación original no especificada en el registro) a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Panitumumab es un anticuerpo monoclonal humano dirigido contra el receptor EGFR, comercializado en Colombia como Vectibix®. El registro sanitario no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto del registro solo repite "PANITUMUMAB") |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 99.13% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Panitumumab es un anticuerpo monoclonal totalmente humano que bloquea el EGFR. Esta señalización participa en la diferenciación de los osteoblastos y en la regulación de la osteoclastogénesis, lo que crea un vínculo teórico con el metabolismo óseo.

Sin embargo, este vínculo es débil y la dirección del efecto es incierta. Los estudios preclínicos sugieren que inhibir el EGFR podría **reducir** la formación de hueso en lugar de protegerlo. El bloqueo del EGFR también causa hipomagnesemia, lo que podría empeorar la salud ósea.

El puntaje alto de TxGNN (0.991) proviene solo de un análisis de grafos. Puede reflejar cercanía en la red biológica y no un beneficio terapéutico real. Por ahora, la predicción no tiene respaldo clínico ni bibliográfico.

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
| 20025916 | VECTIBIX® 20 MG/ML (AMGEN EUROPE B.V.) | Solución concentrada para infusión | PANITUMUMAB (el texto no describe una indicación clínica) |

Nota: el paquete de datos reporta 8 registros en total, pero las 5 entradas recibidas corresponden al mismo número de registro (20025916) y son idénticas, por lo que se muestran una sola vez.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Magnesio y electrolitos (el bloqueo del EGFR causa hipomagnesemia); además, vigilancia de la superficie ocular y la piel |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Advertencias del prospecto INVIMA**: no disponibles en el Evidence Pack (brecha de datos clasificada como bloqueante).
- **Preocupaciones propias de la clase anti-EGFR (del análisis de racionalidad)**:
  - Hipomagnesemia, que podría agravar la salud ósea.
  - Toxicidad de la superficie ocular (ojo seco, queratitis, tricomegalia), relevante para la segunda predicción (retinopatía diabética).

Consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos ni literatura, y la evidencia preclínica sugiere un posible efecto adverso sobre el hueso. La segunda predicción de TxGNN, retinopatía diabética no proliferativa grave (puntaje 99.05%), también es L5 y Hold. Su mecanismo es especulativo y la toxicidad ocular de los anti-EGFR es una preocupación adicional.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es una brecha bloqueante.
- Obtener datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación original aprobada en Colombia, porque el registro solo muestra el nombre del fármaco.
- Revisar estudios preclínicos sobre el efecto del bloqueo del EGFR en osteoblastos y osteoclastos, para determinar si el efecto es protector o perjudicial.
- Verificar la compatibilidad de vía de administración y la similitud con la indicación original, que siguen pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

