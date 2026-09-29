---
layout: default
title: Theophylline
parent: Solo Predicción del Modelo (L5)
nav_order: 383
evidence_level: L5
indication_count: 7
---

# Theophylline
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

# Teofilina: De Obstrucción Reversible de las Vías Respiratorias a Enfermedad Trombótica

## Resumen en Una Frase

La teofilina es una xantina broncodilatadora, utilizada tradicionalmente en asma, enfisema y bronquitis crónica.
El modelo TxGNN predice que podría ser efectiva para **enfermedad trombótica**,
pero actualmente hay **0 ensayos clínicos** y **ninguna publicación con apoyo clínico directo** (las 16 recuperadas son mayormente de otros temas). Es una predicción del modelo sin respaldo experimental.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | AMBROXOL (es el único texto no vacío en los registros; corresponde a un componente de un producto combinado, no a una indicación. Según la base de farmacología, el uso clínico de la teofilina es obstrucción reversible de las vías respiratorias) |
| Nueva Indicación Predicha | Enfermedad trombótica (thrombotic disease) |
| Puntaje de Predicción TxGNN | 99.62% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, la teofilina es un inhibidor no selectivo de las fosfodiesterasas (PDE) y antagonista de los receptores de adenosina (A1, A2A, A2B y A3, según la base de farmacología consultada). Su eficacia en enfermedades obstructivas de las vías respiratorias está establecida, y mecanísticamente podría ser aplicable a la trombosis.

El vínculo propuesto es indirecto. Al inhibir las PDE, la teofilina podría elevar el AMPc plaquetario, lo que en principio tiene un efecto antiplaquetario débil. Un estudio en perros de 1983 (PMID 6313894) mostró que la aminofilina, una sal de teofilina, potenció el efecto antitrombótico de la prostaciclina en un modelo de trombosis coronaria. No demuestra por sí solo un beneficio de la teofilina en humanos.

Las publicaciones recuperadas no ofrecen apoyo clínico. Tratan sobre ticlopidina, métodos de medición plaquetaria y un biosensor de teofilina, y en varias la teofilina solo aparece como reactivo de laboratorio. La alta puntuación del modelo (99.62%) no equivale a evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Se muestran las 10 publicaciones más cercanas al tema entre las 16 recuperadas. Ninguna es un ensayo clínico con teofilina en trombosis.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6313894](https://pubmed.ncbi.nlm.nih.gov/6313894/) | 1983 | Preclínico (perro) | J Pharmacol Exp Ther | La aminofilina potenció el efecto antitrombótico de la prostaciclina en un modelo canino de trombosis coronaria. Es la señal más cercana a la hipótesis. |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Estudio in vitro | Gen Pharmacol | Milrinona y adenosina inhiben la respuesta plaquetaria humana mediante AMPc. Apoya el mecanismo, no la teofilina en sí. |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Revisión | CRC Crit Rev Biochem | Revisa el equilibrio entre tromboxano A2 y prostaciclina, y el papel del AMPc plaquetario en la aterosclerosis. |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Revisión | Clin Pharmacokinet | Farmacocinética de la ticlopidina, un antiagregante. No trata de teofilina. |
| [26764324](https://pubmed.ncbi.nlm.nih.gov/26764324/) | 2016 | Estudio in vitro | J Nutr | El extracto de ajo envejecido inhibe la agregación plaquetaria por vías de AMPc/GMPc. No involucra teofilina. |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohorte | Rheumatology (Oxford) | Activación plaquetaria y de neutrófilos en la enfermedad de Behçet. Relación indirecta. |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Estudio observacional | Inflamm Bowel Dis | Formación de agregados plaqueta-leucocito en la enfermedad inflamatoria intestinal. Relación indirecta. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Método de laboratorio | Br J Haematol | Radioinmunoensayo del factor plaquetario 4. La teofilina solo se usa como aditivo del anticoagulante de la muestra. |
| [29220362](https://pubmed.ncbi.nlm.nih.gov/29220362/) | 2017 | Método de laboratorio | PLoS One | Preparación óptima de plasma para medir moléculas plaquetarias. Sin relación terapéutica. |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Método de laboratorio | Cells | Efecto de la anticoagulación y el procesamiento de muestras sobre la cuantificación de microARN sanguíneos. Sin relación terapéutica. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20005160 | TRIATUSIC® JARABE (LABQUIFAR LTDA.) | Jarabe | Ambroxol; Dextrometorfano (el campo lista componentes, no indicaciones) |

Los datos entregados solo detallan este producto (con filas repetidas en el registro), aunque el total de registros sanitarios es 20. La información de los otros no está disponible en este informe.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta devolvió 4 registros, pero corresponden a dianas farmacológicas (receptores de adenosina A1, A2A, A2B y A3), no a interacciones con otros medicamentos. No hay datos de interacciones entre fármacos en este paquete.
- **Margen terapéutico estrecho**: la literatura recuperada señala que la teofilina tiene una ventana terapéutica estrecha y requiere monitoreo de sus niveles por su toxicidad a concentraciones altas (PMID 29254574, PMID 27844172). Otras predicciones del mismo paquete mencionan interacciones con inhibidores de CYP1A2, macrólidos y quinolonas.

Para advertencias y contraindicaciones formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura recuperada no respalda un efecto de la teofilina en trombosis. Solo existe un mecanismo plausible pero débil (aumento del AMPc plaquetario) y un estudio preclínico en perros con aminofilina.

**Para avanzar se necesita:**
- Una búsqueda de literatura dirigida (teofilina o aminofilina + agregación plaquetaria, trombosis, tromboembolismo) con evaluación de relevancia real.
- Estudios preclínicos o in vitro de la teofilina sobre agregación plaquetaria en concentraciones terapéuticas.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Datos de mecanismo de acción de DrugBank.
- Confirmar la indicación original en los registros colombianos, ya que el campo actual contiene componentes de un producto combinado.

**Nota sobre otras predicciones del paquete:** la predicción de *enfermedad pulmonar obstructiva* (puntaje 99.48%, nivel L1, "Proceed with Guardrails") corresponde a un uso ya establecido, con varios ensayos de Fase 3 completados (por ejemplo, NCT03984188 y NCT02340520). No es un reposicionamiento nuevo. La predicción de *enfermedad de la cavidad nasal* tiene un ensayo de Fase 2 completado (NCT03990766, n=27) que requiere verificar diseño y resultados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

