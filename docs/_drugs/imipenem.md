---
layout: default
title: Imipenem
parent: Solo Predicción del Modelo (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Imipenem
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

# Imipenem: De Infecciones Bacterianas (antibacteriano carbapenémico) a Esclerodermia Difusa

## Resumen en Una Frase

Imipenem es un antibiótico carbapenémico, comercializado en Colombia en combinación con cilastatina y utilizado para tratar infecciones bacterianas.
El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Imipenem y cilastatina (texto de registro INVIMA; no detalla la indicación) |
| Nueva Indicación Predicha | Esclerodermia difusa |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en el Evidence Pack. Según la información conocida, imipenem es un antibiótico carbapenémico que inhibe las proteínas fijadoras de penicilina (PBP) de la pared bacteriana, y en Colombia se comercializa combinado con cilastatina. Su eficacia está establecida en infecciones bacterianas, no en enfermedades autoinmunes ni fibróticas.

**En este caso la predicción no tiene un fundamento mecanístico plausible.** La esclerodermia difusa (esclerosis sistémica) es una enfermedad autoinmune y fibrosante. Imipenem no tiene actividad antifibrótica ni inmunomoduladora conocida que sea relevante para ella.

El puntaje alto de TxGNN (99.99%) refleja únicamente una predicción del modelo. No hay ensayos clínicos ni literatura que la sustenten, por lo que debe tratarse como una señal computacional sin validación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19982795 | Imipenem y Cilastatina 1 g | Polvo estéril para reconstituir a solución inyectable | Imipenem y cilastatina |

Nota: el Evidence Pack lista cinco entradas idénticas bajo el mismo número de registro (fabricante: Farmalógica S.A.), por lo que se muestra una sola fila. El total de registros informado es 20.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para esclerodermia difusa es solo del modelo (L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible. No hay base para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- El prospecto de INVIMA con advertencias y contraindicaciones, para poder hacer el cribado de seguridad.
- Una hipótesis biológica que conecte un carbapenémico con la fibrosis o la autoinmunidad. Sin ella, no se justifica ningún estudio.

**Otras predicciones del mismo fármaco con más respaldo (para priorización):**
- **Infección por *Staphylococcus aureus*** (nivel L2, TxGNN 99.95%): incluye un ensayo de Fase 4 completado de fosfomicina más imipenem en endocarditis por SARM (NCT00871104, n=50). El ensayo de Fase 3 listado (NCT03583333) no se pudo confirmar como específico para *S. aureus*. La eficacia frente a SARM no es confiable con imipenem solo.
- **Fiebre tifoidea** (nivel L3, TxGNN 99.98%): series retrospectivas sugieren uso de carbapenémicos como agente de reserva en cepas extensamente resistentes (XDR). No hay ensayo prospectivo controlado, y el uso choca con la política de control de carbapenémicos.
- **Salmonelosis** (nivel L4) y **fiebre paratifoidea** (nivel L4): hay datos in vitro y de vigilancia de resistencia, pero ningún resultado clínico específico.

Estas indicaciones son antibacterianas, coherentes con el uso original del fármaco, y merecen evaluación por separado.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

