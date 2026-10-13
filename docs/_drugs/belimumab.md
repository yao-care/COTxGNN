---
layout: default
title: Belimumab
parent: Solo Predicción del Modelo (L5)
nav_order: 97
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

# Belimumab: De Indicación No Especificada a Trastorno de Liberación Primaria de Plaquetas

## Resumen en Una Frase

Belimumab es un anticuerpo monoclonal que neutraliza BLyS (BAFF), registrado en Colombia bajo el nombre comercial Benlysta; en los datos compilados el texto de indicación aprobada solo repite el nombre del principio activo, sin especificar la enfermedad.
El modelo TxGNN predice que podría ser efectivo para el **trastorno de liberación primaria de plaquetas**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro INVIMA solo indica "BELIMUMAB") |
| Nueva Indicación Predicha | Trastorno de liberación primaria de plaquetas |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Belimumab es un anticuerpo monoclonal que neutraliza BLyS (BAFF), con lo que reduce la supervivencia de los linfocitos B y la producción de autoanticuerpos. Los datos compilados no incluyen el mecanismo de acción detallado de DrugBank, por lo que este resumen se basa en el conocimiento general del fármaco.

Los trastornos de liberación primaria de plaquetas suelen ser defectos funcionales hereditarios (secreción de gránulos o señalización plaquetaria) y no están mediados por linfocitos B. **No se aprecia un vínculo mecanístico plausible.** El puntaje de 99.96% es una predicción basada en el grafo de conocimiento y no está respaldada por ningún ensayo ni publicación.

Entre las demás indicaciones predichas, solo la trombocitopenia aloinmune fetal y neonatal (TAIFN) tiene un vínculo biológico teórico, porque está mediada por aloanticuerpos maternos. Aun así, no hay estudios de belimumab en embarazo para esta finalidad, el manejo actual se basa en inmunoglobulina intravenosa (con o sin corticoides) y el paso placentario de anticuerpos IgG plantea dudas de seguridad fetal. Las otras predicciones (seudo-enfermedad de von Willebrand, trombastenia de Glanzmann, retinopatía diabética no proliferativa grave y macrotrombocitopenia autosómica dominante) tampoco cuentan con una justificación mecanística sólida.

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
| 20048122 (cancelado) | Benlysta 120 mg polvo liofilizado concentrado para solución para infusión | Polvo liofilizado para reconstituir a solución inyectable | Belimumab |
| 20066631 (cancelado) | Benlysta 400 mg polvo liofilizado concentrado para solución para infusión | Polvo liofilizado para reconstituir a solución inyectable | Belimumab |

Ambos registros, de GlaxoSmithKline Colombia S.A., figuran como cancelados; no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 69 interacciones en total. Entre las revisadas, las de nivel **mayor** incluyen:
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - Vacuna BCG (cepa Tice, antígeno vivo)

  Las de nivel **moderado** incluyen:
  - Roflumilast
  - Azatioprina
  - Alemtuzumab
  - Anakinra
  - Canakinumab
  - Alefacept
  - Vacunas (toxoide tetánico, ántrax, adenovirus tipo 4, cólera vivo)
  - Candida albicans
  - Bifidobacterium longum infantis

  Las de nivel **menor** corresponden a sales de zinc (acetato, gluconato, sulfato y cloruro).

  En conjunto, el patrón sugiere un riesgo aditivo de inmunosupresión y precaución con vacunas vivas.

- **Consideración adicional:** el paso placentario de anticuerpos IgG y los datos limitados en embarazo son relevantes si se evaluara su uso en TAIFN.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en el modelo, pero no cuenta con ensayos clínicos ni publicaciones, y el mecanismo de BAFF no se relaciona de manera plausible con un defecto funcional plaquetario hereditario. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones, y aclarar la indicación original aprobada.
- Obtener datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura y de registros de ensayos específica para la indicación predicha.
- Si se desea explorar una alternativa, priorizar la TAIFN, evaluando antes la seguridad en embarazo y la transferencia placentaria.
- Confirmar el estado regulatorio actual en Colombia, dado que los dos registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

