---
layout: default
title: Iohexol
parent: Solo Predicción del Modelo (L5)
nav_order: 352
evidence_level: L5
indication_count: 2
---

# Iohexol
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

# Iohexol: De Medio de Contraste Radiológico a Insomnio

## Resumen en Una Frase

Iohexol es un medio de contraste yodado no iónico, utilizado en estudios de imagen radiológica; en el registro sanitario colombiano su indicación aparece simplemente como "IOHEXOL".
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero no existen **ensayos clínicos** ni **publicaciones** que respalden esta dirección.
La predicción se considera un artefacto del modelo, sin evidencia real que la sustente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IOHEXOL (el registro no detalla una indicación clínica; corresponde a un medio de contraste radiológico) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, iohexol es un medio de contraste yodado no iónico, farmacológicamente inerte, que se utiliza para visualizar estructuras en estudios radiológicos y no actúa sobre dianas del sistema nervioso central.

No se identifica una relación plausible entre su uso original (imagenología diagnóstica) y el tratamiento del insomnio. No existe un mecanismo conocido por el cual un agente de contraste pueda intervenir en la regulación del sueño.

El puntaje muy alto del modelo (99.87%) parece ser un artefacto del grafo de conocimiento: no hay mecanismo plausible, ensayos clínicos ni literatura de apoyo. Por ello, la predicción debe tomarse con mucha cautela.

**Otra predicción del modelo: ansiedad (puntaje 99.25%).** Tampoco existe un vínculo farmacológico creíble. La literatura recuperada menciona la ansiedad solo como contexto del procedimiento o como efecto adverso (por ejemplo, tras mielografía), no como un resultado terapéutico. Su nivel de evidencia también es L5 y la recomendación es Hold.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para insomnio.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para insomnio.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20139023 (cancelado) | IOHEXOL INYECCION 300MG/ML | Solución inyectable | IOHEXOL |

El fabricante del único registro es Unique Pharmaceutical Laboratories. No hay registros vigentes.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: Se identificaron 100 interacciones en total. Entre las revisadas, la gran mayoría son de nivel **Mayor** y una de nivel Moderado (manitol). Las principales son:
  - Corticosteroides: hidrocortisona, dexametasona, betametasona, triamcinolona
  - Metformina
  - Anfotericina B (incluida la formulación de complejo lipídico)
  - Aminoglucósidos y glucopéptidos: kanamicina, neomicina, vancomicina
  - Levofloxacino
  - Mesalazina y balsalazida
  - Bupropión, dietilpropión y fentermina
  - Morfina, dronabinol y metoclopramida

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia clínica ni literatura que respalde el uso de iohexol en insomnio, y no hay un mecanismo farmacológico plausible. El puntaje alto de TxGNN se interpreta como un artefacto del grafo, y el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica creíble que vincule el fármaco con el sueño
- Estudios preclínicos que demuestren algún efecto sobre el sistema nervioso central
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones) para completar el análisis de seguridad
- Reevaluar la utilidad de la predicción antes de destinar recursos adicionales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

